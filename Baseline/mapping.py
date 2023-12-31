key_mapping_dict = {
    'marital-status': 0,
    'occupation': 1,
    'relationship': 2,
    'race': 3,
    'sex': 4,
    'education': 5,
    'native-country': 6,
    'workclass': 7,
    'class': 8,
    'education-num': 9,
    'capital-gain' : 10,
    'capital-loss' : 11,
    'hours-per-week' : 12
}

# 映射字典
mapping_dict = {
    'age': 'continuous',
    'workclass': {
        'Private': 0,
        'Self-emp-not-inc': 1,
        'Self-emp-inc': 2,
        'Federal-gov': 3,
        'Local-gov': 4,
        'State-gov': 5,
        'Without-pay': 6,
        'Never-worked': 7
    },
    'fnlwgt': 'continuous',
    'education': {
        'Bachelors': 0,
        'Some-college': 1,
        '11th': 2,
        'HS-grad': 3,
        'Prof-school': 4,
        'Assoc-acdm': 5,
        'Assoc-voc': 6,
        '9th': 7,
        '7th-8th': 8,
        '12th': 9,
        'Masters': 10,
        '1st-4th': 11,
        '10th': 12,
        'Doctorate': 13,
        '5th-6th': 14,
        'Preschool': 15
    },
    'education-num': 'continuous',
    'marital-status': {
        'Married-civ-spouse': 0,
        'Divorced': 1,
        'Never-married': 2,
        'Separated': 3,
        'Widowed': 4,
        'Married-spouse-absent': 5,
        'Married-AF-spouse': 6
    },
    'occupation': {
        'Tech-support': 0,
        'Craft-repair': 1,
        'Other-service': 2,
        'Sales': 3,
        'Exec-managerial': 4,
        'Prof-specialty': 5,
        'Handlers-cleaners': 6,
        'Machine-op-inspct': 7,
        'Adm-clerical': 8,
        'Farming-fishing': 9,
        'Transport-moving': 10,
        'Priv-house-serv': 11,
        'Protective-serv': 12,
        'Armed-Forces': 13
    },
    'relationship': {
        'Wife': 0,
        'Own-child': 1,
        'Husband': 2,
        'Not-in-family': 3,
        'Other-relative': 4,
        'Unmarried': 5
    },
    'race': {
        'White': 0,
        'Asian-Pac-Islander': 1,
        'Amer-Indian-Eskimo': 2,
        'Other': 3,
        'Black': 4
    },
    'sex': {
        'Female': 0,
        'Male': 1
    },
    'capital-gain': 'continuous',
    'capital-loss': 'continuous',
    'hours-per-week': 'continuous',
    'native-country': {
        'United-States': 0,
        'Cambodia': 1,
        'England': 2,
        'Puerto-Rico': 3,
        'Canada': 4,
        'Germany': 5,
        'Outlying-US(Guam-USVI-etc)': 6,
        'India': 7,
        'Japan': 8,
        'Greece': 9,
        'South': 10,
        'China': 11,
        'Cuba': 12,
        'Iran': 13,
        'Honduras': 14,
        'Philippines': 15,
        'Italy': 16,
        'Poland': 17,
        'Jamaica': 18,
        'Vietnam': 19,
        'Mexico': 20,
        'Portugal': 21,
        'Ireland': 22,
        'France': 23,
        'Dominican-Republic': 24,
        'Laos': 25,
        'Ecuador': 26,
        'Taiwan': 27,
        'Haiti': 28,
        'Columbia': 29,
        'Hungary': 30,
        'Guatemala': 31,
        'Nicaragua': 32,
        'Scotland': 33,
        'Thailand': 34,
        'Yugoslavia': 35,
        'El-Salvador': 36,
        'Trinadad&Tobago': 37,
        'Peru': 38,
        'Hong': 39,
        'Holand-Netherlands': 40
    },
    'class': {
        '>50K': 1,
        '<=50K': 0
    }
}



def mapData(File):
    with open(File, "r") as file:
        lines = file.readlines()

    size = 0

    mapped_data = []
    continues_data = []
    # 获取数组的初始大小
    keys = mapping_dict.keys()
    for attribute in list(keys):
        # print(attribute)
        if isinstance(mapping_dict[attribute], dict):
            mapped_data.append([])
        else:
            continues_data.append([])

    # 默认映射规则为-1
    default_mapping = -1

    # print(len(lines))
    index = 0
    index2 = 0
    index3 = 0
    for line in lines:
        values = line.strip().split(", ")
        mapped_values = []

        for i, value in enumerate(values):
            attribute = list(mapping_dict.keys())[i]

            if attribute in mapping_dict:
                if isinstance(mapping_dict[attribute], dict):
                    mapped_data[index].append(mapping_dict[attribute].get(value, default_mapping))
                    index = (index + 1) % len(mapped_data)
                    # 使用默认映射规则来处理未知值
                    # print(attribute)
                    # print(mapping_dict[attribute].get(value, default_mapping))
                    # mapped_values.append(f"{attribute}: {mapping_dict[attribute].get(value, default_mapping)}")
                else:
                    continues_data[index3].append(value)
                    index3 = (index3 + 1) % len(continues_data)
                    # mapped_values.append(f"{attribute}: {mapping_dict[attribute]}")
        #     if index == 8:
        #         index2 = index2 + 1
        #
        # if index2 == 1:
        #     break
    return mapped_data, continues_data
