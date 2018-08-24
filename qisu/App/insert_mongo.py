import os
import re
from copy import deepcopy
import pymongo
from lxml import etree
from datetime import datetime


def strip_tag(s):
    if s:
        fr = re.compile(r'(( )+|(\n)+)', re.S)
        dr = fr.sub(' ', s).replace("&gt;", ">")
        return dr
    return ""


def tranfrom_date(s):
    if s:
        try:
            time_format = datetime.strptime(s, "%B %Y")
        except:
            time_format = datetime.strptime(s, "%B %d, %Y")
        time_format = time_format.strftime('%Y-%m-%d')
        return time_format
    return ""


def gen_find(path):
    stack = []
    stack.append(path)
    fileAbsList = []
    while len(stack) != 0:
        dirpath = stack.pop()
        filesList = os.listdir(dirpath)
        for fileName in filesList:
            fileAbsPath = os.path.join(dirpath, fileName)
            if os.path.isdir(fileAbsPath):
                stack.append(fileAbsPath)
            if not fileAbsPath.endswith(".xml"):
                continue
            else:
                fileAbsList.append(fileAbsPath)
                yield fileAbsPath


def parse_xml(filename):
    d = {}
    if filename.endswith(".xml"):
        with open(filename, "rt", encoding="latin-1") as f:
            temp_list = []
            temp_dict = {}
            xml = f.read()
            xml_parse = etree.HTML(xml)
            d["download_date"] = xml_parse.xpath("//required_header//download_date/text()")[0]
            d["link_text"] = xml_parse.xpath("//required_header//link_text/text()")[0]
            d["url"] = xml_parse.xpath("//required_header//url/text()")[0]
            rg_study_id = xml_parse.xpath("//org_study_id/text()")
            d["rg_study_id"] = "" if rg_study_id == [] else rg_study_id[0]
            nct_id = xml_parse.xpath("//nct_id/text()")
            d["nct_id"] = "" if nct_id == [] else nct_id[0]
            brief_title = xml_parse.xpath("//brief_title/text()")
            d["brief_title"] = "" if brief_title == [] else brief_title[0]
            official_title = xml_parse.xpath("//official_title/text()")
            d["official_title"] = "" if official_title == [] else official_title[0]
            lead_sponsor = xml_parse.xpath("//lead_sponsor/agency/text()")
            temp_dict["lead_sponsor"] = "" if lead_sponsor == [] else lead_sponsor[0]
            collaborator = xml_parse.xpath("//collaborator//agency/text()")
            temp_dict["collaborator"] = "" if collaborator == [] else collaborator[0]
            temp_list.append(temp_dict)
            sponsors_temp = deepcopy(temp_list)
            d["sponsors"] = sponsors_temp
            del temp_list[0:]
            source = xml_parse.xpath("//source/text()")
            d["source"] = "" if source == [] else source[0]
            has_dmc = xml_parse.xpath("//has_dmc/text()")
            temp_dict["has_dmc"] = "" if has_dmc == [] else has_dmc[0]
            is_fda_regulated_drug = xml_parse.xpath("//is_fda_regulated_drug/text()")
            is_fda_regulated_device = xml_parse.xpath("//is_fda_regulated_device/text()")
            temp_dict["is_fda_regulated_drug"] = "" if is_fda_regulated_drug == [] else is_fda_regulated_drug[0]
            temp_dict["is_fda_regulated_device"] = "" if is_fda_regulated_device == [] else is_fda_regulated_device[0]
            temp_list.append(temp_dict)
            oversight_info_temp = deepcopy(temp_list)
            d["oversight_info"] = oversight_info_temp
            del temp_list[0:]
            brief_summary = xml_parse.xpath("//brief_summary//textblock/text()")
            d["brief_summary"] = "" if brief_summary == [] else strip_tag(brief_summary[0])
            detailed_description = xml_parse.xpath("//detailed_description//textblock/text()")
            d["detailed_description"] = "" if detailed_description == [] else strip_tag(detailed_description[0])
            overall_status = xml_parse.xpath("//overall_status/text()")
            d["overall_status"] = "" if overall_status == [] else overall_status[0]
            start_date = xml_parse.xpath("//start_date/text()")
            d["start_date"] = "" if start_date == [] else tranfrom_date(start_date[0])
            completion_date = xml_parse.xpath("//completion_date/text()")
            d["completion_date"] = "" if completion_date == [] else tranfrom_date(completion_date[0])
            primary_completion_date = xml_parse.xpath("//primary_completion_date/text()")
            d["primary_completion_date"] = "" if primary_completion_date == [] else tranfrom_date(
                primary_completion_date[0])
            phase = xml_parse.xpath("//phase/text()")
            d["phase"] = "" if phase == [] else phase[0]
            study_type = xml_parse.xpath("//study_type/text()")
            d["study_type"] = "" if study_type == [] else study_type[0]
            has_expanded_access = xml_parse.xpath("//has_expanded_access/text()")
            d["has_expanded_access"] = "" if has_expanded_access == [] else has_expanded_access[0]
            allocation = xml_parse.xpath("//allocation/text()")
            temp_dict["allocation"] = "" if allocation == [] else allocation[0]

            intervention_model = xml_parse.xpath("//intervention_model/text()")
            temp_dict["intervention_model"] = "" if intervention_model == [] else intervention_model[0]
            intervention_model_description = xml_parse.xpath("//intervention_model_description/text()")
            temp_dict["intervention_model_description"] = "" if intervention_model_description == [] else \
                intervention_model_description[0]
            primary_purpose = xml_parse.xpath("//primary_purpose/text()")
            temp_dict["primary_purpose"] = "" if primary_purpose == [] else primary_purpose[0]
            masking = xml_parse.xpath("//masking/text()")
            temp_dict["masking"] = "" if masking == [] else masking[0]
            masking_description = xml_parse.xpath("//masking_description//text()")
            temp_dict["masking_description"] = "" if masking_description == [] else masking_description[0]
            temp_list.append(temp_dict)
            study_design_info_temp = deepcopy(temp_list)
            study_design_info = study_design_info_temp
            d["study_design_info"] = study_design_info
            del temp_list[0:]
            measure = xml_parse.xpath("//measure/text()")
            d["measure"] = "" if measure == [] else measure[0]
            time_frame = xml_parse.xpath("//time_frame/text()")
            d["time_frame"] = "" if time_frame == [] else time_frame[0]
            description = xml_parse.xpath("//description/text()")
            d["description"] = "" if description == [] else description[0]
            measure = xml_parse.xpath("//measure/text()")
            d["measure"] = "" if measure == [] else measure[0]
            temp = []
            for primary_outcome in xml_parse.xpath("//primary_outcome"):
                q = {}
                measure = primary_outcome.xpath(".//measure//text()")
                q.update(measure="" if measure == [] else measure[0])
                time_frame = primary_outcome.xpath(".//time_frame//text()")
                q.update(time_frame="" if time_frame == [] else time_frame[0])
                description = primary_outcome.xpath(".//description/text()")
                q.update(description="" if description == [] else description[0])
                temp.append(q)
            d["primary_outcome"] = temp
            temp1 = []
            for secondary_outcome in xml_parse.xpath("//secondary_outcome") or xml_parse.xpath("//other_outcome"):
                q = {}
                measure = secondary_outcome.xpath(".//measure//text()")
                q.update(measure="" if measure == [] else measure[0])
                time_frame = secondary_outcome.xpath(".//time_frame//text()")
                q.update(time_frame="" if time_frame == [] else time_frame[0])
                description = secondary_outcome.xpath(".//description/text()")
                q.update(description="" if description == [] else description[0])
                temp1.append(q)
            d["secondary_outcome"] = temp1

            number_of_arms = xml_parse.xpath("//number_of_arms/text()")
            d["number_of_arms"] = "" if number_of_arms == [] else number_of_arms[0]
            enrollment = xml_parse.xpath("//enrollment//text()")
            d["enrollment"] = "" if enrollment == [] else enrollment[0]
            condition = xml_parse.xpath("//condition//text()")
            d["condition"] = "" if condition == [] else condition
            temp2 = []
            for arm_group in xml_parse.xpath("//arm_group"):
                q = {}
                arm_group_label = arm_group.xpath(".//arm_group_label//text()")
                q.update(arm_group_label="" if arm_group_label == [] else arm_group_label[0])
                arm_group_type = arm_group.xpath(".//arm_group_type//text()")
                q.update(arm_group_type="" if arm_group_type == [] else arm_group_type[0])
                description = arm_group.xpath(".//description/text()")
                q.update(description="" if description == [] else description[0])
                temp2.append(q)
            d["arm_group"] = temp2

            temp3 = []
            for intervention in xml_parse.xpath("//intervention"):
                q = {}
                intervention_type = intervention.xpath(".//intervention_type//text()")
                q.update(intervention_type="" if intervention_type == [] else intervention_type[0])
                arm_group_type = intervention.xpath(".//intervention_name//text()")
                q.update(arm_group_type="" if arm_group_type == [] else arm_group_type[0])
                description = intervention.xpath(".//description/text()")
                q.update(description="" if description == [] else description[0])
                arm_group_label = intervention.xpath(".//arm_group_label/text()")
                q.update(arm_group_label="" if arm_group_label == [] else arm_group_label[0])
                temp3.append(q)
            d["intervention"] = temp3

            temp4 = []
            for eligibility in xml_parse.xpath("//eligibility"):
                q = {}
                criteria = eligibility.xpath(".//criteria/textblock/text()")
                q["criteria"] = "" if criteria == [] else strip_tag(criteria[0])
                gender = eligibility.xpath("./gender/text()")
                q.update(gender="" if gender == [] else gender[0])
                minimum_age = eligibility.xpath("./minimum_age/text()")
                q.update(minimum_age="" if minimum_age == [] else minimum_age[0])
                maximum_age = eligibility.xpath("./maximum_age/text()")
                q.update(maximum_age="" if maximum_age == [] else maximum_age[0])
                healthy_volunteers = eligibility.xpath("./healthy_volunteers/text()")
                q.update(healthy_volunteers="" if healthy_volunteers == [] else healthy_volunteers[0])
                temp4.append(q)
            d["eligibility"] = temp4

            temp5 = []
            for overall_contact in xml_parse.xpath("//overall_contact"):
                q = {}
                last_name = overall_contact.xpath("./last_name/text()")
                q.update(last_name="" if last_name == [] else last_name[0])
                phone = overall_contact.xpath("./phone/text()")
                q.update(phone="" if phone == [] else phone[0])
                email = overall_contact.xpath("./email/text()")
                q.update(email="" if email == [] else email[0])
                temp5.append(q)
            d["overall_contact"] = temp5

            temp6 = []
            for overall_contact_backup in xml_parse.xpath("//overall_contact_backup"):
                q = {}
                last_name = overall_contact_backup.xpath("./last_name/text()")
                q.update(last_name="" if last_name == [] else last_name[0])
                phone = overall_contact_backup.xpath("./phone/text()")
                q.update(phone="" if phone == [] else phone[0])
                email = overall_contact_backup.xpath("./email/text()")
                q.update(email="" if email == [] else email[0])
                temp6.append(q)
            d["overall_contact_backup"] = temp6
            verification_date = xml_parse.xpath("//verification_date/text()")
            d["verification_date"] = "" if verification_date == [] else tranfrom_date(verification_date[0])
            study_first_submitted = xml_parse.xpath("//study_first_submitted/text()")
            d["study_first_submitted"] = "" if study_first_submitted == [] else tranfrom_date(study_first_submitted[0])
            study_first_submitted_qc = xml_parse.xpath("//study_first_submitted_qc/text()")
            d["study_first_submitted_qc"] = "" if study_first_submitted_qc == [] else tranfrom_date(
                study_first_submitted_qc[0])
            study_first_posted = xml_parse.xpath("//study_first_posted/text()")
            d["study_first_posted"] = "" if study_first_posted == [] else tranfrom_date(study_first_posted[0])
            last_update_submitted = xml_parse.xpath("//last_update_submitted/text()")
            d["last_update_submitted"] = "" if last_update_submitted == [] else tranfrom_date(last_update_submitted[0])
            last_update_submitted_qc = xml_parse.xpath("//last_update_submitted_qc/text()")
            d["last_update_submitted_qc"] = "" if last_update_submitted_qc == [] else tranfrom_date(
                last_update_submitted_qc[0])
            last_update_posted = xml_parse.xpath("//last_update_posted/text()")
            d["last_update_posted"] = "" if last_update_posted == [] else tranfrom_date(last_update_posted[0])
            temp7 = []
            for responsible_party in xml_parse.xpath("//responsible_party"):
                q = {}
                responsible_party_type = responsible_party.xpath("./responsible_party_type/text()")
                q.update(responsible_party_type="" if responsible_party_type == [] else responsible_party_type[0])
                investigator_affiliation = responsible_party.xpath("./investigator_affiliation/text()")
                q.update(investigator_affiliation="" if investigator_affiliation == [] else investigator_affiliation[0])
                investigator_full_name = responsible_party.xpath("./investigator_full_name/text()")
                q.update(investigator_full_name="" if investigator_full_name == [] else investigator_full_name[0])
                investigator_title = responsible_party.xpath("./investigator_title/text()")
                q.update(investigator_title="" if investigator_title == [] else investigator_title[0])
                temp7.append(q)
            d["responsible_party"] = temp7
            keyword = xml_parse.xpath("//keyword/text()")
            d["keyword"] = "" if keyword == [] else keyword
            condition_browse = xml_parse.xpath("//condition_browse//mesh_term/text()")
            d["condition_browse"] = "" if condition_browse == [] else condition_browse
            intervention_browse = xml_parse.xpath("//intervention_browse//mesh_term/text()")
            d["intervention_browse"] = "" if intervention_browse == [] else intervention_browse
        return d


def insert_MongoDB(datas):
    MONGODB_SERVER = "localhost"
    MONGODB_PORT = 27017
    MONGODB_DB = "cry"
    MONGODB_COLLECTION = "cry"
    client = pymongo.MongoClient(MONGODB_SERVER, MONGODB_PORT)
    db = client[MONGODB_DB]
    collection = db[MONGODB_COLLECTION]
    d = [{
        'download_date': datas["download_date"],
        'link_text': datas["link_text"],
        'url': datas["url"],
        'rg_study_id': datas["rg_study_id"],
        'nct_id': datas["nct_id"],
        'brief_title': datas["brief_title"],
        'official_title': datas["official_title"], 'sponsors': datas["sponsors"],
        'source': datas["source"], 'oversight_info': datas["oversight_info"],
        'brief_summary': datas["brief_summary"],
        'detailed_description': datas["detailed_description"],
        'overall_status': datas["overall_status"], 'start_date': datas["start_date"],
        'completion_date': datas["completion_date"],
        'primary_completion_date': datas["primary_completion_date"],
        'phase': datas["phase"], 'study_type': datas["study_type"],
        'has_expanded_access': datas["has_expanded_access"],
        'study_design_info': datas["study_design_info"], 'measure': datas["measure"],
        'time_frame': datas["time_frame"], 'description': datas["description"],
        'primary_outcome': datas["primary_outcome"],
        'secondary_outcome': datas["secondary_outcome"],
        'number_of_arms': datas["number_of_arms"], 'enrollment': datas["enrollment"],
        'condition': datas["condition"], 'arm_group': datas["arm_group"],
        'intervention': datas["intervention"], 'eligibility': datas["eligibility"],
        'overall_contact': datas["overall_contact"],
        'overall_contact_backup': datas["overall_contact_backup"],
        'verification_date': datas["verification_date"],
        'study_first_submitted': datas["study_first_submitted"],
        'study_first_submitted_qc': datas["study_first_submitted_qc"],
        'study_first_posted': datas["study_first_posted"],
        'last_update_submitted': datas["last_update_submitted"],
        'last_update_submitted_qc': datas["last_update_submitted_qc"],
        'last_update_posted': datas["last_update_posted"],
        'responsible_party': datas["responsible_party"], 'keyword': datas["keyword"],
        'condition_browse': datas["condition_browse"],
        'intervention_browse': datas["intervention_browse"]}]

    if collection.find({"url": datas["url"]}).count() == 0:
        collection.insert_many(d)
    else:
        collection.update_many({"url": datas["url"]},
                               {"$set": {
                                   'download_date': datas["download_date"],
                                   'link_text': datas["link_text"],
                                   'url': datas["url"],
                                   'rg_study_id': datas["rg_study_id"],
                                   'nct_id': datas["nct_id"],
                                   'brief_title': datas["brief_title"],
                                   'official_title': datas["official_title"], 'sponsors': datas["sponsors"],
                                   'source': datas["source"], 'oversight_info': datas["oversight_info"],
                                   'brief_summary': datas["brief_summary"],
                                   'detailed_description': datas["detailed_description"],
                                   'overall_status': datas["overall_status"], 'start_date': datas["start_date"],
                                   'completion_date': datas["completion_date"],
                                   'primary_completion_date': datas["primary_completion_date"],
                                   'phase': datas["phase"], 'study_type': datas["study_type"],
                                   'has_expanded_access': datas["has_expanded_access"],
                                   'study_design_info': datas["study_design_info"], 'measure': datas["measure"],
                                   'time_frame': datas["time_frame"], 'description': datas["description"],
                                   'primary_outcome': datas["primary_outcome"],
                                   'secondary_outcome': datas["secondary_outcome"],
                                   'number_of_arms': datas["number_of_arms"], 'enrollment': datas["enrollment"],
                                   'condition': datas["condition"], 'arm_group': datas["arm_group"],
                                   'intervention': datas["intervention"], 'eligibility': datas["eligibility"],
                                   'overall_contact': datas["overall_contact"],
                                   'overall_contact_backup': datas["overall_contact_backup"],
                                   'verification_date': datas["verification_date"],
                                   'study_first_submitted': datas["study_first_submitted"],
                                   'study_first_submitted_qc': datas["study_first_submitted_qc"],
                                   'study_first_posted': datas["study_first_posted"],
                                   'last_update_submitted': datas["last_update_submitted"],
                                   'last_update_submitted_qc': datas["last_update_submitted_qc"],
                                   'last_update_posted': datas["last_update_posted"],
                                   'responsible_party': datas["responsible_party"], 'keyword': datas["keyword"],
                                   'condition_browse': datas["condition_browse"],
                                   'intervention_browse': datas["intervention_browse"]}})


for filename in gen_find("/Users/xuguoliang/ALLPublicXML"):
    parseData = parse_xml(filename)
    insert_MongoDB(parseData)

# count = 0
# for i in gen_find("/Users/xuguoliang/ALLPublicXML"):
#     print(i)
#     d = parse_xml(i)
#     print(d)
#     count += 1
#     if count == 5000:
#         break








