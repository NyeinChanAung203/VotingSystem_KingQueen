from django.shortcuts import render,redirect,get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.generic import ListView,DetailView
from .models import FirstYear,TheWhole
from django.contrib import messages
from users.models import VotingUser


def index(request):
    context = {'section':'home'}
    return render(request,'king_queen/index.html',context)


class FirstKingListView(ListView):
    model = FirstYear
    template_name = 'king_queen/firstking_list.html'
    context_object_name = 'f_kings'

    def get_queryset(self):
        return FirstYear.objects.filter(gender='King')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['section'] = 'active'
        return context

class FirstQueenListView(ListView):
    model = FirstYear
    template_name = 'king_queen/firstqueen_list.html'
    context_object_name = 'f_queens'

    def get_queryset(self):
        return FirstYear.objects.filter(gender='Queen')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['section'] = 'active'
        return context

class FirstKingDetailView(DetailView):
    model = FirstYear
    template_name = 'king_queen/firstking_detail.html'
    context_object_name = 'f_king'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['section'] = 'active'
        return context

class FirstQueenDetailView(DetailView):
    model = FirstYear
    template_name = 'king_queen/firstqueen_detail.html'
    context_object_name = 'f_queen'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['section'] = 'active'
        return context

def FirstKingVote(request,pk):
    if request.method == 'POST':
        code = request.POST
        print(code['qrcode'])
        if len(code['qrcode']) == 32:
            try:
                check_code = VotingUser.objects.get(qr_code=code['qrcode'])
                if check_code.vote_first_king > 0:

                    # Decreasing voting attempt and save obj
                    print(check_code.name,check_code.qr_code,check_code.vote_first_king)
                    check_code.vote_first_king -= 1
                    check_code.save()
                    print(check_code.name,check_code.qr_code,check_code.vote_first_king)

                    #Adding votes to related user(king&queen)
                    first_king = get_object_or_404(FirstYear,pk=pk)
                    print(first_king.name,first_king.gender,first_king.votes)
                    first_king.votes += 1
                    first_king.save()
                    print(first_king.name,first_king.gender,first_king.votes)
                    messages.success(request,'Successfully voted!')
                    return redirect('index')    
                else:
                    messages.warning(request,'You can only vote 1 times for a year.')
                    return redirect('firstking')
            except:
                print('except')
                messages.warning(request,'Wrong Qrcode!')
                return HttpResponseRedirect(reverse('firstkingdetail',args=[pk]))
                
        else:
            messages.warning(request,'Wrong Qrcode!')
            return HttpResponseRedirect(reverse('firstkingdetail',args=[pk]))
        
    else:
        return redirect('index')


def FirstQueenVote(request,pk):
    if request.method == 'POST':
        code = request.POST
        print(code['qrcode'])
        if len(code['qrcode']) == 32:
            try:
                check_code = VotingUser.objects.get(qr_code=code['qrcode'])
                if check_code.vote_first_queen > 0:

                    # Decreasing voting attempt and save obj
                    print(check_code.name,check_code.qr_code,check_code.vote_first_queen)
                    check_code.vote_first_queen -= 1
                    check_code.save()
                    print(check_code.name,check_code.qr_code,check_code.vote_first_queen)

                    #Adding votes to related user(king&queen)
                    first_queen = get_object_or_404(FirstYear,pk=pk)
                    print(first_queen.name,first_queen.gender,first_queen.votes)
                    first_queen.votes += 1
                    first_queen.save()
                    print(first_queen.name,first_queen.gender,first_queen.votes)
                    messages.success(request,'Successfully voted!')
                    return redirect('index')    
                else:
                    messages.warning(request,'You can only vote 1 times for a year.')
                    return redirect('firstqueen')
            except:
                print('except')
                messages.warning(request,'Wrong Qrcode!')
                return HttpResponseRedirect(reverse('firstqueendetail',args=[pk]))
                
        else:
            messages.warning(request,'Wrong Qrcode!')
            return HttpResponseRedirect(reverse('firstqueendetail',args=[pk]))
        
    else:
        return redirect('index')



######################################################
class TheWholeKingListView(ListView):
    model = TheWhole
    template_name = 'king_queen/thewholeking_list.html'
    context_object_name = 't_kings'

    def get_queryset(self):
        return TheWhole.objects.filter(gender='King')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['section'] = 'active'
        return context

class TheWholeQueenListView(ListView):
    model = TheWhole
    template_name = 'king_queen/thewholequeen_list.html'
    context_object_name = 't_queens'

    def get_queryset(self):
        return TheWhole.objects.filter(gender='Queen')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['section'] = 'active'
        return context

class TheWholeKingDetailView(DetailView):
    model = TheWhole
    template_name = 'king_queen/thewholeking_detail.html'
    context_object_name = 't_king'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['section'] = 'active'
        return context

class TheWholeQueenDetailView(DetailView):
    model = TheWhole
    template_name = 'king_queen/thewholequeen_detail.html'
    context_object_name = 't_queen'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['section'] = 'active'
        return context

def TheWholeKingVote(request,pk):
    if request.method == 'POST':
        code = request.POST
        print(code['qrcode'])
        if len(code['qrcode']) == 32:
            try:
                check_code = VotingUser.objects.get(qr_code=code['qrcode'])
                if check_code.vote_king > 0:

                    # Decreasing voting attempt and save obj
                    print(check_code.name,check_code.qr_code,check_code.vote_king)
                    check_code.vote_king -= 1
                    check_code.save()
                    print(check_code.name,check_code.qr_code,check_code.vote_king)

                    #Adding votes to related user(king&queen)
                    the_king = get_object_or_404(TheWhole,pk=pk)
                    print(the_king.name,the_king.gender,the_king.votes)
                    the_king.votes += 1
                    the_king.save()
                    print(the_king.name,the_king.gender,the_king.votes)
                    messages.success(request,'Successfully voted!')
                    return redirect('index')    
                else:
                    messages.warning(request,'You can only vote 1 times for a year.')
                    return redirect('thewholeking')
            except:
                print('except')
                messages.warning(request,'Wrong Qrcode!')
                return HttpResponseRedirect(reverse('thewholekingdetail',args=[pk]))
                
        else:
            messages.warning(request,'Wrong Qrcode!')
            return HttpResponseRedirect(reverse('thewholekingdetail',args=[pk]))
        
    else:
        return redirect('index')


def TheWholeQueenVote(request,pk):
    if request.method == 'POST':
        code = request.POST
        print(code['qrcode'])
        if len(code['qrcode']) == 32:
            try:
                check_code = VotingUser.objects.get(qr_code=code['qrcode'])
                if check_code.vote_queen > 0:

                    # Decreasing voting attempt and save obj
                    print(check_code.name,check_code.qr_code,check_code.vote_queen)
                    check_code.vote_queen -= 1
                    check_code.save()
                    print(check_code.name,check_code.qr_code,check_code.vote_queen)

                    #Adding votes to related user(king&queen)
                    the_queen = get_object_or_404(TheWhole,pk=pk)
                    print(the_queen.name,the_queen.gender,the_queen.votes)
                    the_queen.votes += 1
                    the_queen.save()
                    print(the_queen.name,the_queen.gender,the_queen.votes)
                    messages.success(request,'Successfully voted!')
                    return redirect('index')    
                else:
                    messages.warning(request,'You can only vote 1 times for a year.')
                    return redirect('thewholequeen')
            except:
                print('except')
                messages.warning(request,'Wrong Qrcode!')
                return HttpResponseRedirect(reverse('thewholequeendetail',args=[pk]))
                
        else:
            messages.warning(request,'Wrong Qrcode!')
            return HttpResponseRedirect(reverse('thewholequeendetail',args=[pk]))
        
    else:
        return redirect('index')
