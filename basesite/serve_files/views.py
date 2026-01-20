from django.shortcuts import render, redirect
from .forms import FileTypeForm
from .api_backend.fetch_files import RFile

def index(request):
    return render(request, "base.html")

def file_display(request):
    """
    View for output display of the fetched files. The
    request sessions holds the file list in temp_file_list
    :param request: request
    :return: Returns render request from template
    """
    file_list = request.session.pop('temp_file_list', [])
    context = {'file_list': file_list}
    return render(request, 'display.html', context)

def file_fetch(request):
    """
    View used to gather user input for the local path
    and the type of files to display.
    :param request: form path and file type
    :return: temp_file_list and redirect to display
    """
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = FileTypeForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            f_path = form.cleaned_data['folder_path']
            f_type = form.cleaned_data['file_types']
            # gathers the list of files
            file_list = RFile(f_path, f_type).fetch()
            request.session['temp_file_list'] = file_list

            return redirect('/files/display/')
    else:
        form = FileTypeForm()

    return render(request, 'main.html', {'form': form})