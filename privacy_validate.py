def solution(today, terms, privacies):
    result = []
    
    terms_dict = {}
    for term in terms:
        name, validate = term.split()
        terms_dict[name] = validate
    
    for idx, privacy in enumerate(privacies):
        term_date, term_name = privacy.split()
        validate = terms_dict[term_name]
        year, month, day = term_date.split('.')
        int_month = int(month) + int(validate)
        year = str(int(year) + int_month // 12)
        month = str(int_month % 12)
        if int_month % 12 == 0:
            year = str(int(year) - 1)
            month = '12'
        month = month.rjust(2, '0')
        
        if year+'.'+month+'.'+day <= today:
            result.append(idx+1)
            
    return result

today = "2022.05.19"
terms = ["A 6", "B 12", "C 3"]
privacies = ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]
print(solution(today, terms, privacies))