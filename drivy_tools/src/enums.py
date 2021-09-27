from enum import Enum

from drivy_tools.src.models import CityDetails


class BRAND_NAMES(Enum):
    Alfa_Romeo = "Alfa - Romeo"
    Asia_Motors = "Asia Motors"
    Audi = "Audi"
    Authi = "Authi"
    Automobiles_Grandi = "Automobiles Grandi"
    Azure = "Azure"
    Barkas = "Barkas"
    BMC = "BMC"
    BMW = "BMW"
    Bollore = "Bolloré"
    Borgward = "Borgward"
    Buddy = "Buddy"
    Caterham = "Caterham"
    Chevrolet = "Chevrolet"
    Chrysler = "Chrysler"
    Citroen = "Citroen"
    Corvette = "Corvette"
    Cupra = "Cupra"
    Dacia = "Dacia"
    Daewoo = "Daewoo"
    Daihatsu = "Daihatsu"
    Dangel = "Dangel"
    Dodge = "Dodge"
    Fiat = "Fiat"
    Ford = "Ford"
    FSO = "FSO"
    Gaz = "Gaz"
    Glas = "Glas"
    Honda = "Honda"
    Hotchkiss = "Hotchkiss"
    Hyundai = "Hyundai"
    Infiniti = "Infiniti"
    Isuzu = "Isuzu"
    Iveco = "Iveco"
    Jaguar = "Jaguar"
    Jeep = "Jeep"
    Kia = "Kia"
    Lada = "Lada"
    Lancia = "Lancia"
    Land_Rover = "Land Rover"
    Land_Rover_ = "Land - Rover"
    LDV = "LDV"
    Lexus = "Lexus"
    Lincoln = "Lincoln"
    Lotus = "Lotus"
    LTI = "LTI"
    Mahindra = "Mahindra"
    Man = "Man"
    Maxus = "Maxus"
    Mazda = "Mazda"
    Mega = "Mega"
    Mercedes = "Mercedes"
    Mg = "Mg"
    Mia = "Mia"
    Mini = "Mini"
    Mitsubishi = "Mitsubishi"
    Nissan = "Nissan"
    Oldsmobile = "Oldsmobile"
    Opel = "Opel"
    Panhard = "Panhard"
    Peugeot = "Peugeot"
    Pgo = "Pgo"
    Piaggio = "Piaggio"
    Polestar = "Polestar"
    Renault = "Renault"
    Rover = "Rover"
    Saab = "Saab"
    Santana = "Santana"
    Scion = "Scion"
    Seat = "Seat"
    Simca = "Simca"
    Skoda = "Skoda"
    Smart = "Smart"
    Ssangyong = "Ssangyong"
    Subaru = "Subaru"
    Suzuki = "Suzuki"
    Tata_Motors = "Tata Motors"
    Tesla = "Tesla"
    Toyota = "Toyota"
    Triumph = "Triumph"
    Vauxhall = "Vauxhall"
    Volkswagen = "Volkswagen"
    Volvo = "Volvo"
    Xpeng = "Xpeng"
    Andere = "Andere"


brand_id_map = {
    "99": "Asia_Motors",
    "2": "Alfa_Romeo",
    "5": "Audi",
    "96": "Authi",
    "100": "Automobiles_Grandi",
    "113": "Azure",
    "106": "Barkas",
    "105": "BMC",
    "8": "BMW",
    "88": "Bollore",
    "110": "Borgward",
    "112": "Buddy",
    "11": "Caterham",
    "12": "Chevrolet",
    "14": "Chrysler",
    "15": "Citroen",
    "74": "Corvette",
    "117": "Cupra",
    "16": "Dacia",
    "17": "Daewoo",
    "18": "Daihatsu",
    "75": "Dangel",
    "19": "Dodge",
    "21": "Fiat",
    "22": "Ford",
    "109": "FSO",
    "103": "Gaz",
    "108": "Glas",
    "24": "Honda",
    "102": "Hotchkiss",
    "26": "Hyundai",
    "27": "Infiniti",
    "28": "Isuzu",
    "77": "Iveco",
    "29": "Jaguar",
    "30": "Jeep",
    "31": "Kia",
    "32": "Lada",
    "34": "Lancia",
    "101": "Land_Rover",
    "35": "Land_Rover_",
    "78": "LDV",
    "36": "Lexus",
    "104": "Lincoln",
    "37": "Lotus",
    "107": "LTI",
    "79": "Mahindra",
    "118": "Man",
    "114": "Maxus",
    "39": "Mazda",
    "40": "Mega",
    "41": "Mercedes",
    "42": "Mg",
    "83": "Mia",
    "43": "Mini",
    "44": "Mitsubishi",
    "46": "Nissan",
    "97": "Oldsmobile",
    "47": "Opel",
    "92": "Panhard",
    "48": "Peugeot",
    "49": "Pgo",
    "89": "Piaggio",
    "115": "Polestar",
    "52": "Renault",
    "54": "Rover",
    "55": "Saab",
    "56": "Santana",
    "111": "Scion",
    "57": "Seat",
    "91": "Simca",
    "58": "Skoda",
    "59": "Smart",
    "60": "Ssangyong",
    "61": "Subaru",
    "62": "Suzuki",
    "95": "Tata_Motors",
    "90": "Tesla",
    "64": "Toyota",
    "65": "Triumph",
    "98": "Vauxhall",
    "67": "Volkswagen",
    "68": "Volvo",
    "116": "Xpeng",
    "other": "Andere",
}


class YEARS(Enum):
    YEAR_2021 = "2021"
    YEAR_2020 = "2020"
    YEAR_2019 = "2019"
    YEAR_2018 = "2018"
    YEAR_2017 = "2017"
    YEAR_2015 = "2015"
    YEAR_2014 = "2014"
    YEAR_2013 = "2013"
    YEAR_2012 = "2012"
    YEAR_2011 = "2011"
    YEAR_2010 = "2010"
    YEAR_2009 = "2009"
    YEAR_2008 = "2008"
    YEAR_2007 = "2007"
    YEAR_2006 = "2006"
    YEAR_2005 = "2005"
    YEAR_2004 = "2004"
    YEAR_2003 = "2003"
    YEAR_2002 = "2002"
    YEAR_2001 = "2001"
    YEAR_2000 = "2000"
    YEAR_1999 = "1999"
    BEFORE_1998 = "<1998"


year_id_map = {
    "2021": "YEAR_2021",
    "2020": "YEAR_2020",
    "2019": "YEAR_2019",
    "2018": "YEAR_2018",
    "2017": "YEAR_2017",
    "2015": "YEAR_2015",
    "2014": "YEAR_2014",
    "2013": "YEAR_2013",
    "2012": "YEAR_2012",
    "2011": "YEAR_2011",
    "2010": "YEAR_2010",
    "2009": "YEAR_2009",
    "2008": "YEAR_2008",
    "2007": "YEAR_2007",
    "2006": "YEAR_2006",
    "2005": "YEAR_2005",
    "2004": "YEAR_2004",
    "2003": "YEAR_2003",
    "2002": "YEAR_2002",
    "2001": "YEAR_2001",
    "2000": "YEAR_2000",
    "1999": "YEAR_1999",
    "1998": "BEFORE_1998",
}


class KM(Enum):
    KM_O_15 = "0-15.000 km"
    KM_15_50 = "15-50.000 km"
    KM_50_100 = "50-100.000 km"
    KM_100_150 = "100-150.000 km"
    KM_150_200 = "150-200.000 km"
    KM_200 = "+200.000 km"


km_id_map = {
    "1": "KM_O_15",
    "2": "KM_15_50",
    "3": "KM_50_100",
    "4": "KM_100_150",
    "5": "KM_150_200",
    "6": "KM_200",
}


CITY_GENT = CityDetails(
    name="Gent, Belgié",
    country="BE",
    lat=51.0543422,
    long=3.7174243,
    registration_country="BE",
)
