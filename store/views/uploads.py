from django.shortcuts import render , redirect , HttpResponseRedirect
from django.views import View




class upload(View):

    def get(self, request):
        if request.method=='POST':
            form = CustomerForm(request.POST,request.FILES)
            if form.is_valid():
                Product=form.save(commit=False)
                Product.user = request.user
                Product.save()
                return redirect('index')
        else:

          

        
            return render(request , 'costumer_uploads.html',{'form':form})
