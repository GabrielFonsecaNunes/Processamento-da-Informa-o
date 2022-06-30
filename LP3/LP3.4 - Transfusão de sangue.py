blood_type = ''

for i in range(2):
    blood_type += input()

def is_compatible_blood_donation(blood_type: str = None):
    '''
    Args:
        blood_type (str): The first caracter in this string
        represents the patient's blood type and the second 
        caracter is a donor
    Return:
        compatibility (str): The message if blood is compatible or not 
    '''    
    compatibility = {
            'AA': 'transfusao compativel',
            'AB': 'transfusao incompativel',
            'AO': 'transfusao compativel',
            'AAB': 'transfusao incompativel',

            'BA': 'transfusao incompativel',
            'BB': 'transfusao compativel',
            'BO': 'transfusao compativel',
            'BAB': 'transfusao incompativel',

            'OA': 'transfusao incompativel',
            'OB': 'transfusao incompativel',
            'OO': 'transfusao compativel',
            'OAB': 'transfusao incompativel',

            'ABA': 'transfusao compativel',
            'ABB': 'transfusao compativel',
            'ABO': 'transfusao compativel',
            'ABAB': 'transfusao compativel',           
    }

    return compatibility[blood_type]

print(is_compatible_blood_donation(blood_type = blood_type))