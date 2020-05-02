
def get_info(hospital_list):
    result = []
    for hospital in hospital_list:
        td_list = hospital.find_all("td")
        hospital_info = {}
        for i in range(len(td_list)):
        
            if i%4 == 0:
                city = td_list[i].text
                hospital_info["city"] = city
            elif i%4 ==1:
                district = td_list[i].text
                hospital_info["district"] = district
            elif i%4 ==2:
                if "*" in td_list[i].text:    #*(검체 체취 가능) text 존재시 제거
                    name = td_list[i].text.replace(td_list[i].text[-10:],"").rstrip()
                else:
                    name = td_list[i].text.rstrip()
                hospital_info["name"] = name
            else: 
                contact = td_list[i].text
                hospital_info["contact"] = contact
        result.append(hospital_info)
    return result
