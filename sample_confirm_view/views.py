from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView
from app.forms import BookingForm

class Sample1View(FormView):
    form_class = BookingForm
    success_url = reverse_lazy('sample_confirm_view:sample1_complete')

    def get_template_names(self):
        if self.request.POST.get('step') == 'preview':
            return 'sample_confirm_view/sample1/confirm.html'
        else:
            return 'sample_confirm_view/sample1/form.html'

    def form_valid(self, form):
        if self.request.POST['step'] != 'complete':
            return self.render_to_response(self.get_context_data(form=form))
        return super().form_valid(form)


class Sample1CompleteView(TemplateView):
    template_name = 'sample_confirm_view/sample1/complete.html'

