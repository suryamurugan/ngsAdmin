from django.contrib import admin

from .models import TutionAdmissionFee,Student


# Register your models here.

admin.site.register(Student)
admin.site.site_header = 'Nosegay School'                    # default: "Django Administration"
admin.site.index_title = 'Admin Panel'                 # default: "Site administration"
admin.site.site_title = 'Nosegay' # default: "Django site admin"

@admin.register(TutionAdmissionFee)
class TutionAdmissionFeeAdmin(admin.ModelAdmin):
    #change_list_template = 'admin/sale_summary_change_list.html'
    list_display = ['student_name', 'month','tution_fee','admission_fee','conveyance_fee','total']
    list_editable = ('tution_fee','tution_fee')
    list_filter = ('month',) 
    search_fields = ('student',)
    
    ordering = ['month']

    def student_name(self, obj):
        return obj.student.student_name



    def total(self,obj):
        return str(obj.tution_fee + obj.admission_fee+obj.conveyance_fee)
