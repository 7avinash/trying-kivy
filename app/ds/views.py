from django.shortcuts import render

# Create your views here.
####def vote(request, question_id):
####    p = get_object_or_404(Question, pk= question_id)
####    try:
####        selected_choice = p.choice_set.get(pk = request.POST['choice'])
####    except(KeyError, Choice.DoesNotExist):
####        return render(request, 'polls/details.html', {'question':p, 'error_message': "You didn't select a choice."})
####    else:
####        selected_choice.votes += 1
####        selected_choice.save()
####        return HttpResponseRedirect(reverse('polls:results', args= (p.id,)))
####    
    
    
    

def search(request):
    
    if 'cold' in symptoms_set.all():
        print "hello"