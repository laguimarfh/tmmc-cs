from django.shortcuts import render, HttpResponse
# from django.db.models import Count
from django.views.generic.base import TemplateView
from django.utils import timezone
from django.urls import reverse_lazy 
from django.contrib import messages
from django.views.generic import ListView, DetailView, FormView, CreateView
from . import models
from .filters import SheetFilter
from inputcs.models import Sheet
from inputcs.forms import SheetForm
from django.db.models import Q
# from .models import Journal, Category
from django.forms import HiddenInput
import json

from django.http import HttpResponse, JsonResponse, Http404
# from django.shortcuts import render
# from django.http import HttpResponse
# from django.db.models import 

def sheet_list(request):
    f = SheetFilter(request.GET, queryset=models.Sheet.objects.all())
    return render(request, 'inputcs/template.html', {'filter': f})


class HomeView(ListView):
    """
    The CS homepage
    """
    template_name = 'inputcs/home.html'
    model: Sheet
    context_object_name = 'defects'
    def get_queryset(self):
        return Sheet.objects.all().order_by('-id')[:10]

    # def get_context_data(self, **kwargs):
    #     sheet_form = forms.SheetForm
    #     context = super().get_context_data(**kwargs)
        
    #     context['sheet_form'] = sheet_for
        
    #     return context

class DefectDetailView(DetailView):
    """
    The CS homepage
    """
    model = Sheet
    template_name = 'inputcs/defects_detail.html'
    context_object_name = 'defect'

    # def get_context_data(self, **kwargs):
    #     sheet_form = forms.SheetForm
    #     context = super().get_context_data(**kwargs)
    #     context['sheet_form'] = sheet_form
        
    #     return context


# class InputView(CreateView):
#     """
#     Defect input
#     """
#     model: Sheet
#     template_name = 'inputcs/input.html'
    


class DefectCreateView(CreateView):
    form_class = SheetForm
    template_name = 'inputcs/input2.html'
    
    def get_context_data(self, **kwargs):
        sheet_form = SheetForm
        context = super().get_context_data(**kwargs)
        context['sheet_form'] = sheet_form
        
        return context
    
    # def get_context_data(self, **kwargs):
    #     sheet_form = forms.SheetForm

    #     context = super().get_context_data(**kwargs)
        
    #     context['sheet_form'] = sheet_form
        
    #     return context

# class SheetView(CreateView):
#     model = Sheet
#     success_url: reverse_lazy('inputcs/home.html')
#     fields = [
#         'process',
#         'defect',
#         'period',
#         'coorx',
#         'coory',
#         'photo',
#         'location',
#         'side',
#     ]
#     def form_valid(self, form):
#         messages.add_message(
#             self.request,
#             messages.SUCCESS,
#             'Thank you! Your message has been sent.'
#         )
#         return super().form_valid(form)

# def sheet_form(request):
#     if request.method == "POST":
#         form = forms.SheetForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Contact request submitted successfully.')
#             return render(request, 'home.html', {'form': forms.SheetForm(request.GET)})
#         else:
#             messages.error(request, 'Invalid form submission.')
#             messages.error(request, form.errors)
#     else:
#         form = forms.SheetForm()
#     return render(request, 'input.html', {'form': form})

# class DefectFormView(CreateView):
#     model = models.Sheet
#     success_url = reverse_lazy('home')
    # fields = [
    #     'process',
    #     'defect',
    #     'period',
    #     'coorx',
    #     'coory',
    #     'photo',
    #     'location',
    #     'side',
    # ]
#     if form.is_valid():
#             form.save()
#             messages.success(request, 'Contact request submitted successfully.')
#             return render(request, 'contact-form.html', {'form': SheetForm(request.GET)})
#         else:
#             messages.error(request, 'Invalid form submission.')
#             messages.error(request, form.errors)
#     else:
#         form = ContactForm()
#     return render(request, 'contact-form.html', {'form': form})
    # def form_valid(self, form):
    #     messages.add_message(
    #     self.request,
    #     messages.SUCCESS,
    #     'Thank you! Defect saved'
    # )
    #     return super().form_valid(form)


# def ajaximage(request):
#     coord = models.AjaxImage.objects.order_by('-id')[:5]
#     # context = { 'coord' : coord }
#     form = AjaxImageForm()
#     if request.method == "POST" and request.is_ajax():
#         form = AjaxImageForm(request.POST)
#         if form.is_valid():
#             image_coord = form.cleaned_data['image_coord']
#             form.save()
#             return JsonResponse({"image_coord": image_coord}, status=200)

#     return render(request, "inputcs/imageajax.html", {'form':form})
    

# class AjaxFormView(CreateView):
#     model = models.AjaxImage
#     success_url = reverse_lazy('ajax')
#     fields = [
#         'test',
#     ]
    
#     def form_valid(self, form):
#         messages.add_message(
#             self.request,
#             messages.SUCCESS,
#             'Thank you! Your message has been sent.'
#         )
#         return super().form_valid(form)



def is_valid_queryparam(param):
    return param != '' and param is not None


def bootstrapfilter(request):
    qs = models.Sheet.objects.all()
    categories = models.Sheet.objects.all()
    process_contains_query = request.GET.get('process_contains')
    location_contains_query = request.GET.get('location_contains')
    defect_contains_query = request.GET.get('defect_contains')
    id_exact_query = request.GET.get('id_exact')
    process_or_defect_query = request.GET.get('process_or_defect')
    # view_count_min = request.GET.get('view_count_min')
    # view_count_max = request.GET.get('view_count_max')
    date_min = request.GET.get('date_min')
    date_max = request.GET.get('date_max')
    location_list = request.GET.get('location')
    # reviewed = request.GET.get('reviewed')
    # not_Reviewed = request.GET.get('notReviewed')
    print(
        process_contains_query,
        id_exact_query,
        process_or_defect_query,
        date_max,
        date_min,
        location_list,
        location_contains_query,
        defect_contains_query,
        
        )

    if is_valid_queryparam(process_contains_query):
        qs = qs.filter(process__icontains=process_contains_query)
    
    if is_valid_queryparam(location_contains_query):
        qs = qs.filter(location__icontains=location_contains_query)
    
    if is_valid_queryparam(defect_contains_query):
        qs = qs.filter(defect__icontains=defect_contains_query)

    if is_valid_queryparam(id_exact_query):
        qs = qs.filter(id__exact=id_exact_query)

    elif is_valid_queryparam(process_or_defect_query):
        qs = qs.filter(Q(process__icontains=process_or_defect_query)
                       | Q(author__name__icontains=process_or_defect_query)
                       ).distinct()

    # if is_valid_queryparam(view_count_min):
    #     qs = qs.filter(views__gte=view_count_min)

    # if is_valid_queryparam(view_count_max):
    #     qs = qs.filter(views__lt=view_count_max)

    if is_valid_queryparam(date_min):
        qs = qs.filter(created__gte=date_min)

    if is_valid_queryparam(date_max):
        qs = qs.filter(created__lt=date_max)

    if is_valid_queryparam(location_list) and location_list != 'Choose...':
        qs = qs.filter(location=location_list)

    # if reviewed == 'on':
    #     qs = qs.filter(reviewed=True)
    # elif not_Reviewed == 'on':
    #     qs = qs.filter(reviewed=False)

    context = {
        'queryset': qs,
        
    }
    return render(request, "inputcs/bootstrap_form.html", context)




    # class HomeView2(TemplateView):
#     """
#     The CS homepage2
#     """
#     template_name = 'inputcs/home2.html'

# def create_post(request):
#     if request.method == 'POST':
#         post_text = request.POST.get('the_post')
#         post_coord = request.POST.get('the_coord')
#         response_data = {}

#         post = Post(text=post_text, author=request.user, coord=post_coord)
#         post.save()

#         response_data['result'] = 'Create post successful!'
#         response_data['postpk'] = post.pk
#         response_data['text'] = post.text
#         response_data['coord'] = post.coord
#         response_data['created'] = post.created.strftime('%B %d, %Y %I:%M %p')
#         response_data['author'] = post.author.username

#         return HttpResponse(
#             json.dumps(response_data),
#             content_type="application/json"
#         )
#     else:
#         return HttpResponse(
#             json.dumps({"nothing to see": "this isn't happening"}),
#             content_type="application/json"
#         )
