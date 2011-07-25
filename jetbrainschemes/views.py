from django import forms
from django.http import HttpResponse
import settings
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from jetbrainschemes.models import XmlToPersistence, CssSettings

def index(request):
    selected_scheme = 'twilightest.xml'

#    xmlToPersistence = XmlToPersistence()
#    xmlToPersistence.convert(file_name)

    if request.method == 'POST':
        form = dropdownform(request.POST)
        if form.is_valid():
            selected_scheme = form.cleaned_data['dropdown']

    c = CssSettings.objects.get(file_name=selected_scheme)

    x = dropdownform(initial={"dropdown": c.id})
    return render_to_response('colors/index.html',
                              {'color_schemes': selected_scheme, 'colors': c.css, 'selector': x, 'test': settings.MEDIA_ROOT, 'mediaurl': settings.MEDIA_URL},
                              context_instance=RequestContext(request))


class dropdownform(forms.Form):
    dropdown = forms.ModelChoiceField(queryset = CssSettings.objects.all(), empty_label="(Nothing)")