from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView
from formtools.wizard.views import SessionWizardView
from app.forms import BookingForm
from sample_confirm_view.forms import DummyForm

class Sample1View(FormView):
    '''
    Django FormView ベースの確認画面の実装
    '''
    form_class = BookingForm
    success_url = reverse_lazy('sample_confirm_view:sample1_complete')  # 完了画面

    def get_template_names(self):
        '''
        表示する HTML を決定する。フォーム画面HTMLか、確認画面HTML。
        確認画面HTMLを返す条件は、POST の step で confirm が指定され、フォームバリデーションが成功したとき。
        それ以外は、フォーム画面HTMLを返す。
        '''
        if self.request.POST.get('step') == 'confirm' and self.get_form().is_valid():
            return ['sample_confirm_view/sample1/confirm.html']
        else:
            return ['sample_confirm_view/sample1/form.html']

    def form_valid(self, form):
        '''
        フォームバリデーションが成功したときに実行される。
        入力画面と確認画面でバリデーションが成功しても success_url が実行されないようにする。
        '''
        if self.request.POST['step'] != 'complete':
            return self.render_to_response(self.get_context_data(form=form))
        
        # ここでデータベースに保存
        # self.object = form.save()
        # または
        # Booking.objects.create()

        return super().form_valid(form)


class Sample1CompleteView(TemplateView):
    template_name = 'sample_confirm_view/sample1/complete.html'


class Sample2View(SessionWizardView):
    '''
    サードパーティモジュール django-formtools を使った確認画面の実装
    '''
    FORMS = [
        ('form', BookingForm),
        ('confirm', DummyForm),
    ]
    TEMPLATES = {
        'form': 'sample_confirm_view/sample2/form.html',
        'confirm': 'sample_confirm_view/sample2/confirm.html',
    }

    def get_template_names(self):
        return [self.TEMPLATES[self.steps.current]]

    def get_context_data(self, form, **kwargs):
        context = super().get_context_data(form, **kwargs)
        context['all_cleaned_data'] = self.get_all_cleaned_data()
        return context

    def done(self, form_list, **kwargs):
        all_cleaned_data = self.get_all_cleaned_data()
        # ここでデータベースに保存
        # Booking.objects.create()
        return redirect('sample_confirm_view:sample2_complete')


class Sample2CompleteView(TemplateView):
    template_name = 'sample_confirm_view/sample2/complete.html'


class Sample3View(FormView):
    pass
