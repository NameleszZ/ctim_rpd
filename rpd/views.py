from django.views.generic.list import ListView
from django.urls import reverse_lazy, reverse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import TableOfDisc, TableOfEducators, Group, Chairs, Specialisations
from django.shortcuts import redirect, get_object_or_404, render
from .forms import AssignRpdForm, FileRpdForm, MessageSendForm
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from django.contrib.auth.models import User
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import os
fs = FileSystemStorage(location='/media/files')


def message_send(request, slug):
    form = MessageSendForm(request.POST or None)
    rpd_info = TableOfDisc.objects.get(slug=slug)
    if request.method == 'POST':
        mess = MessageSendForm(request.POST, instance=rpd_info)
        mess.message = request.POST.get('message')
        messag = request.POST.get('message')
        rpd_info.message = messag
        rpd_info.save()
        mess.save()
        return HttpResponseRedirect(reverse('manage_rpd_list'))
    else:
        return render(request, 'main/form.html', {
            'form': form,
            'object': rpd_info})





def file_send(request, slug):
    rpd_info = TableOfDisc.objects.get(slug=slug)
    specialisation = Specialisations.objects.get(code_of_specialisation=rpd_info.specialisation)
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename=fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        rpd_info.content = myfile
        rpd_info.save()
        return HttpResponseRedirect(reverse('manage_rpd_list'))
    return render(request, 'main/edit.html',{'object':rpd_info,'spec':specialisation,})


def list_of_RPD(request):
    objects = TableOfDisc.objects.filter(educator=request.user)
    profile_name = TableOfEducators.objects.filter(user=request.user)
    return render(request, 'main/list.html', {
        'object_list': objects,
        'profile_list': profile_name,
    })

def profile_view(request, slug):
    profile_name = TableOfEducators.objects.get(id=slug.id)
    return render(request, 'main/profile.html', {
        'profile_info': profile_name,
    })


def assign_RPD(request, slug):
    form = AssignRpdForm(request.POST)
    rpd_info = TableOfDisc.objects.get(slug=slug)
    specialisation = Specialisations.objects.get(code_of_specialisation=rpd_info.specialisation)
    user_list = TableOfEducators.objects.all()
    if request.method == 'POST':
        form = AssignRpdForm(request.POST, instance=rpd_info)
        user = request.POST.get('educator')
        comm = request.POST.get('educ_comment')
        stat = request.POST.get('status')
        elem = User.objects.get(id=user)
        rpd_info.educator = elem
        rpd_info.educ_comment = comm
        rpd_info.status = stat
        rpd_info.save()
        return HttpResponseRedirect(reverse('manage_rpd_list'))

    return render(request, 'main/form.html', {
        'form': form,
        'object': rpd_info,'profile_list':user_list,'spec':specialisation,
    })

"""
class CourseModuleUpdateView(TemplateResponseMixin, View):
    template_name = 'main/manage/formset.html'
    course = None

    def get_formset(self, data=None):
        return ModuleFormSet(instance=self.course.slug, data=data)

    def dispatch(self, request, slug):
        self.course = get_object_or_404(TableOfDisc,
                                        educator=request.user)
        return super(CourseModuleUpdateView, self).dispatch(request, slug)

    def get(self, request, *args, **kwargs):
        formset = self.get_formset()
        return self.render_to_response({'course': self.course,
                                        'formset': formset})

    def post(self, request, *args, **kwargs):
        formset = self.get_formset(data=request.POST)
        if formset.is_valid():
            formset.save()
            return redirect('manage_course_list')
        return self.render_to_response({'course': self.course,
                                        'formset': formset})

"""