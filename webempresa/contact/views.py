from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import ContactForm

# Create your views here.

def contact(request):
#    print("tipo de peticion: {}".format(request.method)) 
    
    contact_form = ContactForm()
    
    # con post comprobamos si se ha enviado un dato
    if request.method == "POST":
        # rellenamos la plantilla con la informacion enviada
        contact_form = ContactForm(data=request.POST)

        # validamos que los campos son correctos
        if contact_form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')
            # suponemos que todo ha ido bien, redireccionamos
            # return redirect('/contact/?ok')
            # en lugar de pasarle el valor en crudo usaremos reverse que es como un template tag url, cambia dinamicamente
  
            # enviamos el correo y redireccionamos
            email = EmailMessage(
                # asunto
                "La Caffetiera: Nuevo mensaje de contacto",
                # cuerpo
                f"De {name} <{email}>\n\nEscribio:\n\n{content}",
                # pudieramos poner aqui el nombre de la empresa(origen)
                "no-contestar@inbox.mailtrap.io",
                # lista de correos destino
                ["joelcalanche96@gmail.com"],
                reply_to=[email]
              

            )
            try:
                email.send()
                # todo ha ido bien redireccionamos a ok
                return redirect(reverse('contact') + '?ok')
            except:
                # algo no ha ido bien, redireccionamos a FAIL
                return redirect(reverse('contact') + '?fail')


    return render(request,"contact/contact.html",{'form':contact_form})