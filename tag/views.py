from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response

from tag.models import TagEntry
from tag.forms import TagEditForm

def redirect(request, tag):

    tag_entries = TagEntry.objects.filter(tag=tag)
 
    if tag_entries:
	   return HttpResponseRedirect(tag_entries[0].url)
    else:
	   return edit(request, tag)

def edit(request, tag):

    tag_entries = TagEntry.objects.filter(tag=tag)
    if not tag_entries:
        tag_entry = TagEntry(tag=tag, url='')
    else:
        tag_entry = tag_entries[0]

    if request.method == 'GET':
        form = TagEditForm(initial={'tag': tag_entry.tag, 'url': tag_entry.url})
    elif request.method == 'POST':
    	form = TagEditForm(request.POST)
    	if form.is_valid():
            tag_entry.url = form.cleaned_data['url']
            tag_entry.save()
            return HttpResponseRedirect(tag_entry.url)

    return render_to_response('tag/edit.html', {'tag': tag_entry.tag, 'url': tag_entry.url, 'form': form})