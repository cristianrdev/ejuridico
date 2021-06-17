from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'secretary.html')

def home(request):
    try:
        user = User.objects.get(id = int(request.session['logged_user_id']))
        if user:
            #tareas pendientes , completed = False 
            tasks_pending = user.tasks.all().filter(completed = False)
            #tareas completadas
            tasks_completed = user.tasks.all().filter(completed = True)
            print("=====completed> ", tasks_completed)
            return render(request, 'home.html', {'user': user, 'tasks_pending': tasks_pending, 'tasks_completed': tasks_completed})
        else:
            return redirect("/")
    except:
        return redirect("/")


def lawsuit(request):
    if request.method == "POST":
        #guardar el case(request)
        user = User.objects.get(id = int(request.session['logged_user_id']))
        case(request) = Case.objects.create(name = request.POST['name'], 
                            due_date = request.POST['due_date'],
                            user = user)
        return redirect("/home")   


def lawsuit_detail(request, task_id):
    case (request) = Case.objects.get(id = int(case_id))
    if request.method == "POST": #actualizar case(request)
        formCase = CaseForm(request.POST, instance=case(request))
        if formCase.is_valid():
            completed = request.POST.get('completed', '') == 'on'
            case(request).name = request.POST['name']
            case(request).completed = completed
            case(request).save() #actualizar case(request)
            return redirect('/home')
    else:
        formTask = TaskForm(instance=case(request))
        return render(request, 'task_detail.html' , {'formCase': formCase})