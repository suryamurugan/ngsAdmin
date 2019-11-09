from django.shortcuts import render
from .models import Student,TutionAdmissionFee
from .resources import StudentResource
from tablib import Dataset
import json


# Create your views here.

def simple_upload(request):
    data = '''[
  {
    "s_no": 1,
    "student_name": "NAVDEEP KAUR",
    "father_name": "MR.JASWANT SINGH",
    "mother_name": "MRS.INDERJEET KAUR",
    "contact_number": 9568558188,
    "class_std": 1,
    "category": "",
    "blood_group": "",
    "conveyance": "True",
    "address": "KHAMARIYA,NANAKMATTA"
  },
  {
    "s_no": 2,
    "student_name": "PARWINDER KAUR",
    "father_name": "MR.SATNAM SINGH",
    "mother_name": "MRS.JASVINDER KAUR",
    "contact_number": 7500374175,
    "class_std": 1,
    "category": "OBC",
    "blood_group": "",
    "conveyance": "False",
    "address": "PACHPERA BHATTA"
  },
  {
    "s_no": 3,
    "student_name": "KHUSPREET KAUR",
    "father_name": "MR.SATNAM SINGH",
    "mother_name": "MRS.JASVINDER KAUR",
    "contact_number": 7500374175,
    "class_std": 1,
    "category": "OBC",
    "blood_group": "",
    "conveyance": "False",
    "address": "PACHPERA BHATTA"
  },
  {
    "s_no": 4,
    "student_name": "SAMARJEET SINGH",
    "father_name": "MR.SATNAM SINGH",
    "mother_name": "MRS.JASVINDER KAUR",
    "contact_number": 7500374175,
    "class_std": 1,
    "category": "OBC",
    "blood_group": "",
    "conveyance": "False",
    "address": "PACHPERA BHATTA"
  },
  {
    "s_no": 5,
    "student_name": "ADITI RANA",
    "father_name": "MR.SOHAN SINGH RANA",
    "mother_name": "MRS.RINKU DEVI",
    "contact_number": 8193847372,
    "class_std": 1,
    "category": "ST",
    "blood_group": "",
    "conveyance": "True",
    "address": "MILAK NAJEER,NANAKMATTA"
  },
  {
    "s_no": 6,
    "student_name": "KAWALDEEP SINGH",
    "father_name": "MR.RANDHEER SINGH",
    "mother_name": "MRS.PARAMJEET KAUR",
    "contact_number": 9639207475,
    "class_std": 1,
    "category": "OBC",
    "blood_group": "",
    "conveyance": "True",
    "address": "BADHAIYA"
  },
  {
    "s_no": 7,
    "student_name": "RUPSI RANA",
    "father_name": "MR.ARVIND SINGH RANA",
    "mother_name": "MRS.SEEMA RANA",
    "contact_number": 9917091854,
    "class_std": 1,
    "category": "ST",
    "blood_group": "",
    "conveyance": "True",
    "address": "TAPEDA,NANAKMATTA"
  },
  {
    "s_no": 8,
    "student_name": "HASMEET SINGH",
    "father_name": "MR.AJEET SINGH",
    "mother_name": "MRS.KAWALJEET KAUR",
    "contact_number": 9756861302,
    "class_std": 1,
    "category": "GENERAL",
    "blood_group": "",
    "conveyance": "True",
    "address": "OMKAR RICE MILL,NANAKMATTA"
  },
  {
    "s_no": 9,
    "student_name": "RAJ KUMAR SHARMA",
    "father_name": "MR. SHIV KUMAR SHARMA",
    "mother_name": "MRS.MITHLESH SHARMA",
    "contact_number": 9720356275,
    "class_std": 1,
    "category": "GENERAL",
    "blood_group": "",
    "conveyance": "True",
    "address": "MAIN MARKET,NANAKMATTA"
  },
  {
    "s_no": 10,
    "student_name": "PRABHJOT SINGH",
    "father_name": "MR.BAAG SINGH",
    "mother_name": "MRS.JITENDER KAUR",
    "contact_number": 9002638984,
    "class_std": 1,
    "category": "OBC",
    "blood_group": "O+",
    "conveyance": "True",
    "address": "SALMATTA"
  },
  {
    "s_no": 11,
    "student_name": "SHIVANSHU CHAND",
    "father_name": "MR.MANOJ CHAND",
    "mother_name": "MRS.SONI CHAND",
    "contact_number": "7017365262(9870943978)",
    "class_std": 1,
    "category": "GENERAL",
    "blood_group": "A+",
    "conveyance": "True",
    "address": "SUNKHARIKALA,NAGLA"
  },
  {
    "s_no": 12,
    "student_name": "ATHARV VISHWAKARMA",
    "father_name": "MR.VIVEK SHARMA",
    "mother_name": "MRS.RUMA VISHWAKARMA",
    "contact_number": "9756930225(6395613595)",
    "class_std": 1,
    "category": "OBC",
    "blood_group": "",
    "conveyance": "True",
    "address": "MAIN MARKET NANAKMATTA"
  },
  {
    "s_no": 13,
    "student_name": "YUVRAJ SINGH TURNA",
    "father_name": "MR.JASPAL SINGH",
    "mother_name": "MRS.SANDEEP KAUR",
    "contact_number": "8449330922(8057187131)",
    "class_std": 1,
    "category": "GENERAL",
    "blood_group": "",
    "conveyance": "True",
    "address": "MAIN MARKET NANAKMATTA"
  },
  {
    "s_no": 14,
    "student_name": "RAJAT SAHANI",
    "father_name": "MR.GUDDU SAHANI",
    "mother_name": "MRS.YASHODA DEVI",
    "contact_number": "9557349444(8936919088)",
    "class_std": 2,
    "category": "",
    "blood_group": "",
    "conveyance": "True",
    "address": "NAUSHAR,NANAKMATTA"
  },
  {
    "s_no": 15,
    "student_name": "EKNOOR DHANJU",
    "father_name": "MR. CHARANJEET SINGH",
    "mother_name": "MRS. NAVNEET KAUR",
    "contact_number": "7500038894(9756824294)",
    "class_std": 2,
    "category": "",
    "blood_group": "O+",
    "conveyance": "True",
    "address": "PRATAPUR,NANAKMATTA"
  },
  {
    "s_no": 16,
    "student_name": "SARGUNPREET KAUR",
    "father_name": "MR. SATNAM SINGH",
    "mother_name": "MRS.RAMANJOT KAUR",
    "contact_number": 9627655501,
    "class_std": 2,
    "category": "OBC",
    "blood_group": "AB+",
    "conveyance": "True",
    "address": "DEENNAGAR,NANAKMATTA"
  },
  {
    "s_no": 17,
    "student_name": "TANAY",
    "father_name": "MR.SURESH CHANDR",
    "mother_name": "MRS.MAMTA",
    "contact_number": 9927644771,
    "class_std": 2,
    "category": "OBC",
    "blood_group": "O+",
    "conveyance": "True",
    "address": "MAIN MARKET NANAKMATTA"
  },
  {
    "s_no": 18,
    "student_name": "UTKARSH RANA",
    "father_name": "MR.BITTU RANA",
    "mother_name": "MRS.MITHILESH KUMARI",
    "contact_number": "9639652787(9639321684)",
    "class_std": 2,
    "category": "ST",
    "blood_group": "",
    "conveyance": "True",
    "address": "DHYANPUR,KARGARA"
  },
  {
    "s_no": 19,
    "student_name": "ANSHPREET SINGH",
    "father_name": "MR.BALVEER SINGH",
    "mother_name": "MRS.SOMA KAUR",
    "contact_number": 9368566627,
    "class_std": 2,
    "category": "OBC",
    "blood_group": "",
    "conveyance": "True",
    "address": "PACHPERA ,P.O:NANAKMATTA"
  },
  {
    "s_no": 20,
    "student_name": "ANGEL RANA",
    "father_name": "MR.NIVASH SINGH",
    "mother_name": "MRS.RAJWATI RANA",
    "contact_number": "9756824954(9756624954)",
    "class_std": 2,
    "category": "ST",
    "blood_group": "",
    "conveyance": "True",
    "address": "BHARONI,LAMAKHERA,SITARGANJ"
  },
  {
    "s_no": 21,
    "student_name": "AKSHRA RANA",
    "father_name": "MR.SURENDRA SINGH RANA",
    "mother_name": "MRS.RAJESHWARI RANA",
    "contact_number": "9368210331(8630372840)",
    "class_std": 2,
    "category": "ST",
    "blood_group": "",
    "conveyance": "True",
    "address": "OPPOSITE KOTWALI,NANAKMATTA"
  },
  {
    "s_no": 22,
    "student_name": "AISHLEEN KAUR",
    "father_name": "MR.TANJEET SINGH",
    "mother_name": "MRS.SUKHVEER KAUR",
    "contact_number": 8449493127,
    "class_std": 2,
    "category": "GENERAL",
    "blood_group": "",
    "conveyance": "True",
    "address": "MAIN MARKET NANAKMATTA"
  },
  {
    "s_no": 23,
    "student_name": "RAJNI GOSWAMI",
    "father_name": "MR.RAJENDAR GIRI",
    "mother_name": "MRS.KIRAN GOSWAMI",
    "contact_number": 9897609924,
    "class_std": 2,
    "category": "OBC",
    "blood_group": "",
    "conveyance": "True",
    "address": "KALYANPUR ,NANAKMATTA"
  },
  {
    "s_no": 24,
    "student_name": "NIHARIKA RANA",
    "father_name": "MR.VINOD RANA",
    "mother_name": "MRS.SAVITA RANA",
    "contact_number": "8923553450(7536020354)",
    "class_std": 2,
    "category": "ST",
    "blood_group": "",
    "conveyance": "True",
    "address": "SARONJA,LAMAKHERA,(DEHLA ROAD)"
  },
  {
    "s_no": 25,
    "student_name": "SUKIRAT SINGH",
    "father_name": "MR.BALJINDER SINGH",
    "mother_name": "MRS.MANDEEP KAUR",
    "contact_number": 9927317403,
    "class_std": 3,
    "category": "GENERAL",
    "blood_group": "",
    "conveyance": "True",
    "address": "DHOOMKHERA,MAJHOLA"
  },
  {
    "s_no": 26,
    "student_name": "YASH VERMA",
    "father_name": "MR.SURAJPAL VERMA",
    "mother_name": "MRS.RAKHI VERMA",
    "contact_number": "9436446539(9012767901)",
    "class_std": 3,
    "category": "OBC",
    "blood_group": "",
    "conveyance": "False",
    "address": "PACHPERA ,P.O:NANAKMATTA"
  },
  {
    "s_no": 27,
    "student_name": "SONAKSHI KATHAYAT",
    "father_name": "MR.PURAN SINGH KATHAYAT",
    "mother_name": "MRS.VIMLA DEVI",
    "contact_number": 8938937345,
    "class_std": 3,
    "category": "GENERAL",
    "blood_group": "",
    "conveyance": "True",
    "address": "BIDORI,NANAKMATTA"
  },
  {
    "s_no": 28,
    "student_name": "GURSIRAT KAUR",
    "father_name": "MR. SATNAM SINGH",
    "mother_name": "MRS.RAMANJOT KAUR",
    "contact_number": 9627655501,
    "class_std": 3,
    "category": "OBC",
    "blood_group": "B+",
    "conveyance": "True",
    "address": "DEENNAGAR,NANAKMATTA"
  },
  {
    "s_no": 29,
    "student_name": "DILPREET SINGH",
    "father_name": "MR.HARVINDER SINGH",
    "mother_name": "MRS.PARAMJEET KAUR",
    "contact_number": "9837387802(8630126306)",
    "class_std": 3,
    "category": "GENERAL",
    "blood_group": "",
    "conveyance": "True",
    "address": "PRATPUR NO.4,NANAKMATTA"
  },
  {
    "s_no": 30,
    "student_name": "VIVEK SINGH",
    "father_name": "MR.NARESH SINGH",
    "mother_name": "MRS.PARVEEN DEVI",
    "contact_number": 9568348924,
    "class_std": 3,
    "category": "S.T",
    "blood_group": "",
    "conveyance": "True",
    "address": "BHARONI,SITARGANJ"
  },
  {
    "s_no": 31,
    "student_name": "MUKUL RANA",
    "father_name": "MR.KISHOR KUMAR RANA",
    "mother_name": "MRS.PUSHPA RANA",
    "contact_number": "9568477497(9783383753)",
    "class_std": 3,
    "category": "GENERAL",
    "blood_group": "",
    "conveyance": "True",
    "address": "NANAKMATTA MAIN MARKET"
  },
  {
    "s_no": 32,
    "student_name": "AARVI CHAND",
    "father_name": "MR.LALIT CHAND",
    "mother_name": "MRS.VIMLA CHAND",
    "contact_number": "9953441770(9761409972)",
    "class_std": 3,
    "category": "GENERAL",
    "blood_group": "",
    "conveyance": "True",
    "address": "SUNKHARIKALA,NANAKMATTA"
  },
  {
    "s_no": 33,
    "student_name": "KARTIK SINGHAL",
    "father_name": "MR.VINAY KUMAR",
    "mother_name": "MRS. DEEPIKA RANI",
    "contact_number": 9837342271,
    "class_std": 4,
    "category": "GENERAL",
    "blood_group": "O+",
    "conveyance": "True",
    "address": "BIJLI COLONY,NANAKMATTA"
  },
  {
    "s_no": 34,
    "student_name": "JEEVAN GIRI",
    "father_name": "MR.RAJENDAR GIRI",
    "mother_name": "MRS.KIRAN GOSWAMI",
    "contact_number": 9897609924,
    "class_std": 4,
    "category": "OBC",
    "blood_group": "",
    "conveyance": "True",
    "address": "KALYANPUR ,NANAKMATTA"
  },
  {
    "s_no": 35,
    "student_name": "AVNEET KAUR",
    "father_name": "MR.SUKHDEV SINGH",
    "mother_name": "MRS.RAJVINDER KAUR",
    "contact_number": 7983898817,
    "class_std": 4,
    "category": "",
    "blood_group": "",
    "conveyance": "True",
    "address": ""
  },
  {
    "s_no": 36,
    "student_name": "PIYUSH RANA",
    "father_name": "MR.KISHOR KUMAR RANA",
    "mother_name": "MRS.PUSHPA RANA",
    "contact_number": "9568477497(9783383753)",
    "class_std": 4,
    "category": "GENERAL",
    "blood_group": "",
    "conveyance": "True",
    "address": "NANAKMATTA MAIN MARKET"
  },
  {
    "s_no": 37,
    "student_name": "JASKIRT KAUR",
    "father_name": "MR.BAAG SINGH",
    "mother_name": "MRS.JITENDER KAUR",
    "contact_number": 9002638984,
    "class_std": "LKG",
    "category": "OBC",
    "blood_group": "O+",
    "conveyance": "True",
    "address": "SALMATTA"
  },
  {
    "s_no": 38,
    "student_name": "GURKIRAT KAUR",
    "father_name": "MR.BHUPENDRA SINGH",
    "mother_name": "MRS.SUMANDEEP KAUR",
    "contact_number": 7906162212,
    "class_std": "LKG",
    "category": "OBC",
    "blood_group": "",
    "conveyance": "True",
    "address": "PRATAPUR NO.5,NANAKMATTA"
  },
  {
    "s_no": 39,
    "student_name": "ANTARPREET SINGH",
    "father_name": "MR.PRAKASH SINGH",
    "mother_name": "MRS.KULWANT KAUR",
    "contact_number": 9990991313,
    "class_std": "LKG",
    "category": "GENERAL",
    "blood_group": "",
    "conveyance": "True",
    "address": "PACHPERA ,P.O:NANAKMATTA"
  },
  {
    "s_no": 40,
    "student_name": "SHIVANSHI CHAND",
    "father_name": "MR.MANOJ CHAND",
    "mother_name": "MRS.SONI CHAND",
    "contact_number": "7017365262(9870943978)",
    "class_std": "LKG",
    "category": "GENERAL",
    "blood_group": "A",
    "conveyance": "True",
    "address": "SUNKHARIKALA,NAGLA"
  },
  {
    "s_no": 41,
    "student_name": "AKSH SINGHAL",
    "father_name": "MR.VINAY KUMAR",
    "mother_name": "MRS. DEEPIKA RANI",
    "contact_number": 9837342271,
    "class_std": "LKG",
    "category": "GENERAL",
    "blood_group": "O+",
    "conveyance": "True",
    "address": "BIJLI COLONY,NANAKMATTA"
  },
  {
    "s_no": 42,
    "student_name": "LAKSH SINGHAL",
    "father_name": "MR.VINAY KUMAR",
    "mother_name": "MRS. DEEPIKA RANI",
    "contact_number": 9837342271,
    "class_std": "LKG",
    "category": "GENERAL",
    "blood_group": "O+",
    "conveyance": "True",
    "address": "BIJLI COLONY,NANAKMATTA"
  },
  {
    "s_no": 43,
    "student_name": "YOGITA RANA",
    "father_name": "MR. HARIMOHAN SINGH RANA",
    "mother_name": "MRS. KAMLESH RANA",
    "contact_number": "9837612349(7534842906)",
    "class_std": "LKG",
    "category": "ST",
    "blood_group": "",
    "conveyance": "True",
    "address": "BIDORA MAJHOLA"
  },
  {
    "s_no": 44,
    "student_name": "JASKIRAT SINGH",
    "father_name": "",
    "mother_name": "MRS.JASPREET KAUR",
    "contact_number": 9927671274,
    "class_std": "LKG",
    "category": "OBC",
    "blood_group": "O-",
    "conveyance": "True",
    "address": "ETOVA,NANAKMATTA"
  },
  {
    "s_no": 45,
    "student_name": "AKSHIT",
    "father_name": "MR.SURESH CHANDR",
    "mother_name": "MRS.MAMTA",
    "contact_number": 9927644771,
    "class_std": "LKG",
    "category": "OBS",
    "blood_group": "O+",
    "conveyance": "True",
    "address": "MAIN MARKET NANAKMATTA"
  },
  {
    "s_no": 46,
    "student_name": "JASKIRAT KAUR",
    "father_name": "MR.BALVEER SINGH",
    "mother_name": "MRS.MANPREET KAUR",
    "contact_number": 8191978851,
    "class_std": "LKG",
    "category": "",
    "blood_group": "",
    "conveyance": "True",
    "address": ""
  },
  {
    "s_no": 47,
    "student_name": "MOHD.SHUMAILE",
    "father_name": "MR.TAUFEEQ AHMAD",
    "mother_name": "MRS FARHEEN",
    "contact_number": "8527780957(9837585455)",
    "class_std": "LKG",
    "category": "OBC",
    "blood_group": "",
    "conveyance": "False",
    "address": "DYODI"
  },
  {
    "s_no": 48,
    "student_name": "LAKSHYA SHAH",
    "father_name": "MR.SANDEEP SHAH",
    "mother_name": "MRS.VANDANA RANI",
    "contact_number": 7895679911,
    "class_std": "NC",
    "category": "OBC",
    "blood_group": "",
    "conveyance": "True",
    "address": "TAPEDA,NANAKMATTA"
  },
  {
    "s_no": 49,
    "student_name": "DAKSHITA CHANDOLA",
    "father_name": "MR.PRASHANT CHANDOLA",
    "mother_name": "MRS.DEEPIKA CHANDOLA",
    "contact_number": "9814457088(8872251923)",
    "class_std": "NC",
    "category": "GENERAL",
    "blood_group": "B+",
    "conveyance": "True",
    "address": "TAPERA,NANKMATTA"
  },
  {
    "s_no": 50,
    "student_name": "KAUSHAL SAHANI",
    "father_name": "MR.GUDDU SAHANI",
    "mother_name": "MRS.YASHODA DEVI",
    "contact_number": "9557349444(8936919088)",
    "class_std": "NC",
    "category": "",
    "blood_group": "",
    "conveyance": "True",
    "address": "NAUSHAR,NANAKMATTA"
  },
  {
    "s_no": 51,
    "student_name": "ANSH RANA",
    "father_name": "MR.AMIT KUMAR SINGH",
    "mother_name": "MRS.PARSEEN RANA",
    "contact_number": 9927222492,
    "class_std": "NC",
    "category": "ST",
    "blood_group": "B+",
    "conveyance": "True",
    "address": "MAGARSARA,MATIYAI"
  },
  {
    "s_no": 52,
    "student_name": "KASHISH SAGAR",
    "father_name": "MR.SARVESH KUMAR",
    "mother_name": "MRS.ARTI SAGAR",
    "contact_number": "7248729954(7055320111)",
    "class_std": "NC",
    "category": "SC",
    "blood_group": "",
    "conveyance": "True",
    "address": "DEHLA ROAD,TAPEDA"
  },
  {
    "s_no": 53,
    "student_name": "YUGANSH RANA",
    "father_name": "MR.OMKAR SINGH",
    "mother_name": "MRS.NIRMALA RANA",
    "contact_number": 8958787907,
    "class_std": "NC",
    "category": "ST",
    "blood_group": "",
    "conveyance": "True",
    "address": "BHARONI,LAMAKHERA,SITARGANJ"
  },
  {
    "s_no": 54,
    "student_name": "DEVANSHI RANA",
    "father_name": "MR.SURENDRA SINGH RANA",
    "mother_name": "MRS.RAJESHWARI RANA",
    "contact_number": "9368210331(8630372840)",
    "class_std": "NC",
    "category": "ST",
    "blood_group": "",
    "conveyance": "True",
    "address": "OPPOSITE KOTWALI,NANAKMATTA"
  },
  {
    "s_no": 55,
    "student_name": "GURPREET SINGH",
    "father_name": "MR.HARVINDER SINGH",
    "mother_name": "MRS.PARAMJEET KAUR",
    "contact_number": "9837387802(8630126306)",
    "class_std": "NC",
    "category": "GENERAL",
    "blood_group": "",
    "conveyance": "True",
    "address": "PRATPUR NO.4,NANAKMATTA"
  },
  {
    "s_no": 56,
    "student_name": "RUDRA SINGH",
    "father_name": "MR.PANKAJ SINGH",
    "mother_name": "MRS.SEEMA DEVI",
    "contact_number": "9997808717(9027113134)",
    "class_std": "NC",
    "category": "GENERAL",
    "blood_group": "",
    "conveyance": "True",
    "address": "NAGLA NANAKMATTA"
  },
  {
    "s_no": 57,
    "student_name": "TEJASV KHURANA",
    "father_name": "MR.PANKAJ KHURANA",
    "mother_name": "MRS.NISHA KHURANA",
    "contact_number": "9997432411(7088832411)",
    "class_std": "NC",
    "category": "GENERAL",
    "blood_group": "",
    "conveyance": "True",
    "address": "SHISHU MANDIR GALLI,NANAKMATTA"
  },
  {
    "s_no": 58,
    "student_name": "TANVI KHURANA",
    "father_name": "MR.PANKAJ KHURANA",
    "mother_name": "MRS.NISHA KHURANA",
    "contact_number": "9997432411(7088832411)",
    "class_std": "NC",
    "category": "GENERAL",
    "blood_group": "",
    "conveyance": "True",
    "address": "SHISHU MANDIR GALLI,NANAKMATTA"
  },
  {
    "s_no": 59,
    "student_name": "ARADHYA RANA",
    "father_name": "MR.BIJENDRA RANA",
    "mother_name": "MRS.KANCHAN RANA",
    "contact_number": "",
    "class_std": "NC",
    "category": "",
    "blood_group": "",
    "conveyance": "True",
    "address": "PACHPERA ,BHATTA,P.O:NANAKMATTA"
  },
  {
    "s_no": 60,
    "student_name": "MANAS",
    "father_name": "MR.NAVISH RANA",
    "mother_name": "MRS.ANURADHA DEVI",
    "contact_number": 9756924232,
    "class_std": "NC",
    "category": "ST",
    "blood_group": "",
    "conveyance": "True",
    "address": "NAUSHAR,PATTIYA NANAKMATTA"
  },
  {
    "s_no": 61,
    "student_name": "ISHMEET SINGH",
    "father_name": "MR.INDERJEET SINGH",
    "mother_name": "MRS.PARAMJEET KAUR",
    "contact_number": "9758230214(9761930414)",
    "class_std": "NC",
    "category": "OBC",
    "blood_group": "",
    "conveyance": "True",
    "address": "BADHAIYA"
  },
  {
    "s_no": 62,
    "student_name": "ANKITA CHAND",
    "father_name": "MR.DEEPAK CHAND",
    "mother_name": "MRS.DIVYA CHAND",
    "contact_number": 9837207653,
    "class_std": "NC",
    "category": "GENERAL",
    "blood_group": "",
    "conveyance": "True",
    "address": "SIDDHA,NANAKMATTA"
  },
  {
    "s_no": 63,
    "student_name": "GURBAKSH SINGH",
    "father_name": "MR.RESHAM SINGH",
    "mother_name": "MRS.PREET KAUR",
    "contact_number": 9756486675,
    "class_std": "NC",
    "category": "GENERAL",
    "blood_group": "",
    "conveyance": "True",
    "address": "GARIPATTI,NANAKMATTA"
  },
  {
    "s_no": 64,
    "student_name": "MANIK",
    "father_name": "MR. MANGAL SINGH",
    "mother_name": "MRS. KOMAL RANA",
    "contact_number": "6396743013(6398801988)",
    "class_std": "NC",
    "category": "ST",
    "blood_group": "",
    "conveyance": "False",
    "address": "KHAIRNA,BICHPURI"
  },
  {
    "s_no": 65,
    "student_name": "MAX",
    "father_name": "MR. MANGAL SINGH",
    "mother_name": "MRS. KOMAL RANA",
    "contact_number": "6396743013(6398801988)",
    "class_std": "NC",
    "category": "ST",
    "blood_group": "",
    "conveyance": "False",
    "address": "KHAIRNA,BICHPURI"
  },
  {
    "s_no": 66,
    "student_name": "NISHANT RANA",
    "father_name": "MR.PUSHPENDRA SINGH",
    "mother_name": "MRS.SANGEETA DEVI",
    "contact_number": "8077929366(9368010315)",
    "class_std": "NC",
    "category": "ST",
    "blood_group": "",
    "conveyance": "False",
    "address": "KHAIRNA,BICHPURI"
  },
  {
    "s_no": 67,
    "student_name": "JASHANPREET KAUR",
    "father_name": "MR.RANDHEER SINGH",
    "mother_name": "MRS.PARAMJEET KAUR",
    "contact_number": 9639207475,
    "class_std": "NC",
    "category": "OBC",
    "blood_group": "",
    "conveyance": "True",
    "address": "BADHAIYA"
  },
  {
    "s_no": 68,
    "student_name": "HARPREET SINGH",
    "father_name": "MR.KULDEEP SINGH",
    "mother_name": "MRS MEET KAUR",
    "contact_number": 8958467018,
    "class_std": "NC",
    "category": "OBC",
    "blood_group": "",
    "conveyance": "True",
    "address": "JHANKAT"
  },
  {
    "s_no": 69,
    "student_name": "NISHANT RANA",
    "father_name": "MR.MAHESH SINGH",
    "mother_name": "MRS.RINKU DEVI",
    "contact_number": 8923438646,
    "class_std": "NC",
    "category": "ST",
    "blood_group": "",
    "conveyance": "True",
    "address": "PURANGARH,NANAKMATTA"
  },
  {
    "s_no": 70,
    "student_name": "NAVYA RANA",
    "father_name": "MR.PREMRAJ SINGH",
    "mother_name": "MRS.LAXMI RANA",
    "contact_number": 8193859534,
    "class_std": "NC",
    "category": "ST",
    "blood_group": "",
    "conveyance": "True",
    "address": "NAVINAGAR,NANAKMATTA"
  },
  {
    "s_no": 71,
    "student_name": "VIHAN MONGA",
    "father_name": "MR.JAIKAPIL MONGA",
    "mother_name": "MRS.MEET MONGA",
    "contact_number": 8449243700,
    "class_std": "PNC",
    "category": "GENERAL",
    "blood_group": "",
    "conveyance": "True",
    "address": "NANAKMATTA"
  },
  {
    "s_no": 72,
    "student_name": "JAIDITYA ARORA",
    "father_name": "MR.MOHIT ARORA",
    "mother_name": "MRS.NAINA ARORA",
    "contact_number": 9568215013,
    "class_std": "PNC",
    "category": "GENERAL",
    "blood_group": "",
    "conveyance": "True",
    "address": "NANAKMATTA"
  },
  {
    "s_no": 73,
    "student_name": "AGAM BATRA",
    "father_name": "MR.ANKUR BATRA",
    "mother_name": "MRS. KIRAN BATRA",
    "contact_number": 9837365026,
    "class_std": "PNC",
    "category": "GENERAL",
    "blood_group": "",
    "conveyance": "True",
    "address": "MAIN MARKET NANAKMATTA"
  },
  {
    "s_no": 74,
    "student_name": "MANVEER SINGH",
    "father_name": "MR.BALJEET SINGH",
    "mother_name": "MRS.RAJWINDER KAUR",
    "contact_number": "7055662715(9027058225)",
    "class_std": "PNC",
    "category": "OBC",
    "blood_group": "",
    "conveyance": "True",
    "address": "DUYORI"
  },
  {
    "s_no": 75,
    "student_name": "PRABHLEEN KAUR",
    "father_name": "MR.MANDEEP SINGH",
    "mother_name": "MRS.SEERAT KAUR",
    "contact_number": 8171815555,
    "class_std": "PNC",
    "category": "OBC",
    "blood_group": "",
    "conveyance": "False",
    "address": "MAIN MARKET,NEAR BALAJI MANDIR"
  },
  {
    "s_no": 76,
    "student_name": "ISHIKA RANA",
    "father_name": "MR. SUMIT RANA",
    "mother_name": "MRS.RANJU RANA",
    "contact_number": "8077399489(96392231170",
    "class_std": "PNC",
    "category": "ST",
    "blood_group": "",
    "conveyance": "False",
    "address": "BIDORA MAJHOLA"
  },
  {
    "s_no": 77,
    "student_name": "VIVEK SAHANI",
    "father_name": "MR.GUDDU SAHANI",
    "mother_name": "MRS.YASHODA DEVI",
    "contact_number": "9557349444(8936919088)",
    "class_std": "UKG",
    "category": "",
    "blood_group": "",
    "conveyance": "True",
    "address": "NAUSHAR,NANAKMATTA"
  },
  {
    "s_no": 78,
    "student_name": "JAIPREET SINGH",
    "father_name": "MR.JAGDEEP SINGH",
    "mother_name": "MRS.KAMALJEET KAUR",
    "contact_number": "8475876092,(7906593818)",
    "class_std": "UKG",
    "category": "GENERAL",
    "blood_group": "",
    "conveyance": "True",
    "address": "DHOOMKHERA,MAJHOLA"
  },
  {
    "s_no": 79,
    "student_name": "PRANAV SHARMA",
    "father_name": "MR.GAGANDEEP SHARMA",
    "mother_name": "MRS.SARITA SHARMA",
    "contact_number": "9897746308,(9758903200)",
    "class_std": "UKG",
    "category": "GENERAL",
    "blood_group": "",
    "conveyance": "True",
    "address": "PACHPERA ,P.O:NANAKMATTA"
  },
  {
    "s_no": 80,
    "student_name": "NAVNEET KAUR",
    "father_name": "MR.DALJEET SINGH",
    "mother_name": "MRS.CHHINDER KAUR",
    "contact_number": "8780130246,(6396476605)",
    "class_std": "LKG",
    "category": "OBC",
    "blood_group": "",
    "conveyance": "True",
    "address": "JHANKAT(NANAKMATTA)"
  },
  {
    "s_no": 81,
    "student_name": "JASKARAN SINGH",
    "father_name": "MR.BALJEET SINGH",
    "mother_name": "MRS.RAJWINDER KAUR",
    "contact_number": "7055662715(9027058225)",
    "class_std": "UKG",
    "category": "OBC",
    "blood_group": "",
    "conveyance": "True",
    "address": "DUYORI"
  },
  {
    "s_no": 82,
    "student_name": "DAKSHDEEP SINGH",
    "father_name": "MR.NIRMAL SINGH",
    "mother_name": "MRS.SANDEEP KAUR",
    "contact_number": "9917208415(9756061583)",
    "class_std": "UKG",
    "category": "OBC",
    "blood_group": "",
    "conveyance": "True",
    "address": "MOHAMADGANJ NANAKMATTA"
  },
  {
    "s_no": 83,
    "student_name": "GURNEMAT KAUR",
    "father_name": "MR.JERNAIL SINGH",
    "mother_name": "MRS.KULDEEP KAUR",
    "contact_number": "7500718444(7500952697)",
    "class_std": "UKG",
    "category": "",
    "blood_group": "",
    "conveyance": "True",
    "address": "GADIPATTI,NANAKMATTA"
  },
  {
    "s_no": 84,
    "student_name": "NAVPREET KAUR",
    "father_name": "MR.AMREEK SINGH",
    "mother_name": "MRS.GURPREET KAUR",
    "contact_number": 6395514735,
    "class_std": "UKG",
    "category": "GENERAL",
    "blood_group": "",
    "conveyance": "True",
    "address": "SALMATTA"
  },
  {
    "s_no": 85,
    "student_name": "AGARTA",
    "father_name": "MR.SHUBHASH CHANDRA",
    "mother_name": "MRS.SANGEETA DEVI",
    "contact_number": "8938003493(6397478322)",
    "class_std": "UKG",
    "category": "SC",
    "blood_group": "",
    "conveyance": "True",
    "address": "DOHARI,SITARGANJ"
  },
  {
    "s_no": 86,
    "student_name": "PRAGTI RANA",
    "father_name": "MR.SATYAVAN SINGH",
    "mother_name": "MRS.POONAM DEVI",
    "contact_number": "9927207350(7017591107)",
    "class_std": "UKG",
    "category": "ST",
    "blood_group": "",
    "conveyance": "True",
    "address": "AUDALI"
  },
  {
    "s_no": 87,
    "student_name": "ARSHLEEN KAUR",
    "father_name": "MR.PARAMJEET SINGH",
    "mother_name": "MRS.MANDEEP KAUR",
    "contact_number": 7017691388,
    "class_std": "UKG",
    "category": "GENERAL",
    "blood_group": "",
    "conveyance": "True",
    "address": "DEHLA ROAD,NANAKMATTA"
  },
  {
    "s_no": 88,
    "student_name": "AVIJOT SINGH",
    "father_name": "MR.YADVENDER SINGH",
    "mother_name": "MRS.AMANDEEP KAUR",
    "contact_number": 9193260244,
    "class_std": "LKG",
    "category": "",
    "blood_group": "",
    "conveyance": "True",
    "address": "PISTOR NANAKMATTA"
  },
  {
    "s_no": 89,
    "student_name": "UTKARSH BASERA",
    "father_name": "MR.ARJUN SINGH",
    "mother_name": "MRS.KIRAN BASERA",
    "contact_number": 7830344111,
    "class_std": 1,
    "category": "GENERAL",
    "blood_group": "",
    "conveyance": "True",
    "address": "DEHLA ROAD,NANAKMATTA"
  },
  {
    "s_no": 90,
    "student_name": "ANSHDEEP SINGH",
    "father_name": "MR.SARVJEET SINGH",
    "mother_name": "MRS.NAVDEEP KAUR",
    "contact_number": 8476060609,
    "class_std": 3,
    "category": "",
    "blood_group": "",
    "conveyance": "True",
    "address": "PIPALIYA PISTOR,NANAKMATTA"
  },
  {
    "s_no": 91,
    "student_name": "AKSH SINGH BASERA",
    "father_name": "MR.ARJUN SINGH BASERA",
    "mother_name": "MRS.KIRAN BASERA",
    "contact_number": 7830344111,
    "class_std": 4,
    "category": "GENERAL",
    "blood_group": "",
    "conveyance": "True",
    "address": "DEHLA ROAD,NANAKMATTA"
  },
  {
    "s_no": 92,
    "student_name": "VAISHNAVI SAXENA",
    "father_name": "MR.PRIYESH SAXENA",
    "mother_name": "MRS.NEETU SAXENA",
    "contact_number": "9720107210(7351626608)",
    "class_std": 4,
    "category": "",
    "blood_group": "",
    "conveyance": "True",
    "address": "DEHLA ROAD,NANAKMATTA"
  },
  {
    "s_no": 93,
    "student_name": "KIRANDEEP KAUR",
    "father_name": "MR.SUKHVINDER SINGH",
    "mother_name": "MRS.RAMANDEEP KAUR",
    "contact_number": 7500827912,
    "class_std": 4,
    "category": "",
    "blood_group": "",
    "conveyance": "True",
    "address": "NANAKMATTA MANDI"
  },
  {
    "s_no": 94,
    "student_name": "LOVEJOT SINGH",
    "father_name": "MR.SUKHVINDER SINGH",
    "mother_name": "MRS.RAMANDEEP KAUR",
    "contact_number": 7500827912,
    "class_std": 2,
    "category": "",
    "blood_group": "",
    "conveyance": "True",
    "address": "NANKMATTA MANDI"
  },
  {
    "s_no": 95,
    "student_name": "HARMEET SINGH",
    "father_name": "MR.AJEET SINGH SOODAN",
    "mother_name": "MRS.KAVALJEET KAUR",
    "contact_number": 9756861302,
    "class_std": 1,
    "category": "GENERAL",
    "blood_group": "",
    "conveyance": "True",
    "address": "H.N-673,KHATIMA ROAD NANAKMATTA"
  },
  {
    "s_no": 96,
    "student_name": "AYUSHI CHAUHAN",
    "father_name": "MR.HIMANCHAL KUMAR",
    "mother_name": "MRS.NEERAJ RANI",
    "contact_number": "9927335318(7500028953)",
    "class_std": "NC",
    "category": "GENERAL",
    "blood_group": "",
    "conveyance": "True",
    "address": "OPPOSITE THANA,NANAKMATTA"
  },
  {
    "s_no": 97,
    "student_name": "VAIBHAV PHULARA",
    "father_name": "MR. HEMCHANDRA PHULARA",
    "mother_name": "MRS. NISHA PHULARA",
    "contact_number": "9927397564(9756141857)",
    "class_std": "UKG",
    "category": "GENERAL",
    "blood_group": "",
    "conveyance": "True",
    "address": "NEAR UCO BANK,NANAKMATTA"
  }
]'''
    y = json.loads(data)
    for i in y:
        print(i)
        Student.objects.create(s_no=i['s_no'],student_name=i['student_name'],father_name=i['father_name'],mother_name=i['mother_name'],contact_number=i['contact_number'],class_std=i['class_std'],category=i['category'],blood_group=i['blood_group'],conveyance=i['conveyance'],address=i['address'])
        

def simple_upload2(request):
    if request.method == 'POST':
        print("INSIDE UPLOAD")
        person_resource = StudentResource()
        dataset = Dataset()
        print("Inside data")
        print(dataset)

        new_persons = request.FILES['myfile']
        

        imported_data = dataset.load(new_persons.read())
        print("import")
        print(imported_data)
        result = person_resource.import_data(dataset, dry_run=True)  # Test the data import
        print("result")
        print(result)
        print(result.has_errors())
        person_resource.import_data(dataset, dry_run=False)  # Actually import now

        if not result.has_errors():
            person_resource.import_data(dataset, dry_run=False)  # Actually import now

    return render(request, 'school/simple_upload.html')