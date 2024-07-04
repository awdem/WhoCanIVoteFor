from django import template
from django.utils.safestring import mark_safe

register = template.Library()

gss_to_hex = {
    "E14001074": {
        "n": "Barnsley North",
        "r": -23,
        "q": 57,
    },
    "E14001075": {
        "n": "Barnsley South",
        "r": -23,
        "q": 58,
    },
    "E14001083": {
        "n": "Beckenham and Penge",
        "r": -43,
        "q": 65,
    },
    "E14001086": {
        "n": "Bethnal Green and Stepney",
        "r": -39,
        "q": 65,
    },
    "E14001090": {
        "n": "Bicester and Woodstock",
        "r": -34,
        "q": 59,
    },
    "E14001092": {
        "n": "Birmingham Edgbaston",
        "r": -33,
        "q": 53,
    },
    "E14001093": {
        "n": "Birmingham Erdington",
        "r": -31,
        "q": 54,
    },
    "E14001094": {
        "n": "Birmingham Hall Green and Moseley",
        "r": -32,
        "q": 55,
    },
    "E14001095": {
        "n": "Birmingham Hodge Hill and Solihull North",
        "r": -31,
        "q": 55,
    },
    "E14001096": {
        "n": "Birmingham Ladywood",
        "r": -32,
        "q": 54,
    },
    "E14001097": {
        "n": "Birmingham Northfield",
        "r": -34,
        "q": 54,
    },
    "E14001098": {
        "n": "Birmingham Perry Barr",
        "r": -31,
        "q": 53,
    },
    "E14001099": {
        "n": "Birmingham Selly Oak",
        "r": -33,
        "q": 54,
    },
    "E14001100": {
        "n": "Birmingham Yardley",
        "r": -32,
        "q": 56,
    },
    "E14001103": {
        "n": "Blackley and Middleton South",
        "r": -23,
        "q": 53,
    },
    "E14001104": {
        "n": "Blackpool North and Fleetwood",
        "r": -18,
        "q": 53,
    },
    "E14001106": {
        "n": "Blaydon and Consett",
        "r": -14,
        "q": 55,
    },
    "E14001107": {
        "n": "Blyth and Ashington",
        "r": -12,
        "q": 55,
    },
    "E14001111": {
        "n": "Bolton South and Walkden",
        "r": -22,
        "q": 52,
    },
    "E14001122": {
        "n": "Brent East",
        "r": -38,
        "q": 61,
    },
    "E14001123": {
        "n": "Brent West",
        "r": -38,
        "q": 60,
    },
    "E14001126": {
        "n": "Bridgwater",
        "r": -41,
        "q": 48,
    },
    "E14001127": {
        "n": "Bridlington and The Wolds",
        "r": -20,
        "q": 63,
    },
    "E14001128": {
        "n": "Brigg and Immingham",
        "r": -24,
        "q": 62,
    },
    "E14001129": {
        "n": "Brighton Kemptown and Peacehaven",
        "r": -45,
        "q": 67,
    },
    "E14001130": {
        "n": "Brighton Pavilion",
        "r": -44,
        "q": 67,
    },
    "E14001131": {
        "n": "Bristol Central",
        "r": -38,
        "q": 51,
    },
    "E14001133": {
        "n": "Bristol North East",
        "r": -37,
        "q": 51,
    },
    "E14001134": {
        "n": "Bristol North West",
        "r": -38,
        "q": 50,
    },
    "E14001135": {
        "n": "Bristol South",
        "r": -39,
        "q": 51,
    },
    "E14001136": {
        "n": "Broadland and Fakenham",
        "r": -27,
        "q": 66,
    },
    "E14001137": {
        "n": "Bromley and Biggin Hill",
        "r": -42,
        "q": 67,
    },
    "E14001138": {
        "n": "Bromsgrove",
        "r": -33,
        "q": 52,
    },
    "E14001139": {
        "n": "Broxbourne",
        "r": -35,
        "q": 66,
    },
    "E14001140": {
        "n": "Broxtowe",
        "r": -27,
        "q": 59,
    },
    "E14001141": {
        "n": "Buckingham and Bletchley",
        "r": -34,
        "q": 60,
    },
    "E14001142": {
        "n": "Burnley",
        "r": -19,
        "q": 55,
    },
    "E14001143": {
        "n": "Burton and Uttoxeter",
        "r": -28,
        "q": 56,
    },
    "E14001144": {
        "n": "Bury North",
        "r": -21,
        "q": 53,
    },
    "E14001145": {
        "n": "Bury South",
        "r": -22,
        "q": 53,
    },
    "E14001146": {
        "n": "Bury St Edmunds and Stowmarket",
        "r": -31,
        "q": 68,
    },
    "E14001147": {
        "n": "Calder Valley",
        "r": -20,
        "q": 56,
    },
    "E14001148": {
        "n": "Camborne and Redruth",
        "r": -45,
        "q": 43,
    },
    "E14001149": {
        "n": "Cambridge",
        "r": -30,
        "q": 65,
    },
    "E14001150": {
        "n": "Cannock Chase",
        "r": -29,
        "q": 54,
    },
    "E14001151": {
        "n": "Canterbury",
        "r": -41,
        "q": 71,
    },
    "E14001152": {
        "n": "Carlisle",
        "r": -14,
        "q": 53,
    },
    "E14001153": {
        "n": "Carshalton and Wallington",
        "r": -43,
        "q": 62,
    },
    "E14001154": {
        "n": "Castle Point",
        "r": -36,
        "q": 69,
    },
    "E14001155": {
        "n": "Central Devon",
        "r": -42,
        "q": 47,
    },
    "E14001156": {
        "n": "Central Suffolk and North Ipswich",
        "r": -29,
        "q": 68,
    },
    "E14001157": {
        "n": "Chatham and Aylesford",
        "r": -40,
        "q": 69,
    },
    "E14001158": {
        "n": "Cheadle",
        "r": -26,
        "q": 55,
    },
    "E14001159": {
        "n": "Chelmsford",
        "r": -33,
        "q": 67,
    },
    "E14001160": {
        "n": "Chelsea and Fulham",
        "r": -40,
        "q": 61,
    },
    "E14001161": {
        "n": "Cheltenham",
        "r": -36,
        "q": 52,
    },
    "E14001162": {
        "n": "Chesham and Amersham",
        "r": -36,
        "q": 59,
    },
    "E14001163": {
        "n": "Chester North and Neston",
        "r": -28,
        "q": 50,
    },
    "E14001164": {
        "n": "Chester South and Eddisbury",
        "r": -27,
        "q": 51,
    },
    "E14001165": {
        "n": "Chesterfield",
        "r": -26,
        "q": 59,
    },
    "E14001166": {
        "n": "Chichester",
        "r": -44,
        "q": 60,
    },
    "E14001167": {
        "n": "Chingford and Woodford Green",
        "r": -35,
        "q": 64,
    },
    "E14001168": {
        "n": "Chippenham",
        "r": -39,
        "q": 52,
    },
    "E14001169": {
        "n": "Chipping Barnet",
        "r": -36,
        "q": 62,
    },
    "E14001170": {
        "n": "Chorley",
        "r": -20,
        "q": 53,
    },
    "E14001171": {
        "n": "Christchurch",
        "r": -42,
        "q": 53,
    },
    "E14001172": {
        "n": "Cities of London and Westminster",
        "r": -40,
        "q": 63,
    },
    "E14001173": {
        "n": "City of Durham",
        "r": -16,
        "q": 55,
    },
    "E14001174": {
        "n": "Clacton",
        "r": -32,
        "q": 69,
    },
    "E14001175": {
        "n": "Clapham and Brixton Hill",
        "r": -42,
        "q": 62,
    },
    "E14001176": {
        "n": "Colchester",
        "r": -32,
        "q": 68,
    },
    "E14001177": {
        "n": "Colne Valley",
        "r": -23,
        "q": 55,
    },
    "E14001178": {
        "n": "Congleton",
        "r": -27,
        "q": 54,
    },
    "E14001179": {
        "n": "Corby and East Northamptonshire",
        "r": -30,
        "q": 62,
    },
    "E14001180": {
        "n": "Coventry East",
        "r": -33,
        "q": 57,
    },
    "E14001181": {
        "n": "Coventry North West",
        "r": -33,
        "q": 56,
    },
    "E14001182": {
        "n": "Coventry South",
        "r": -34,
        "q": 57,
    },
    "E14001183": {
        "n": "Cramlington and Killingworth",
        "r": -12,
        "q": 56,
    },
    "E14001184": {
        "n": "Crawley",
        "r": -44,
        "q": 69,
    },
    "E14001185": {
        "n": "Crewe and Nantwich",
        "r": -27,
        "q": 53,
    },
    "E14001186": {
        "n": "Croydon East",
        "r": -42,
        "q": 65,
    },
    "E14001187": {
        "n": "Croydon South",
        "r": -43,
        "q": 64,
    },
    "E14001188": {
        "n": "Croydon West",
        "r": -43,
        "q": 63,
    },
    "E14001189": {
        "n": "Dagenham and Rainham",
        "r": -37,
        "q": 67,
    },
    "E14001190": {
        "n": "Darlington",
        "r": -17,
        "q": 55,
    },
    "E14001191": {
        "n": "Dartford",
        "r": -40,
        "q": 68,
    },
    "E14001192": {
        "n": "Daventry",
        "r": -32,
        "q": 60,
    },
    "E14001193": {
        "n": "Derby North",
        "r": -28,
        "q": 58,
    },
    "E14001194": {
        "n": "Derby South",
        "r": -28,
        "q": 57,
    },
    "E14001195": {
        "n": "Derbyshire Dales",
        "r": -26,
        "q": 57,
    },
    "E14001196": {
        "n": "Dewsbury and Batley",
        "r": -22,
        "q": 57,
    },
    "E14001197": {
        "n": "Didcot and Wantage",
        "r": -38,
        "q": 54,
    },
    "E14001198": {
        "n": "Doncaster Central",
        "r": -23,
        "q": 60,
    },
    "E14001199": {
        "n": "Doncaster East and the Isle of Axholme",
        "r": -23,
        "q": 61,
    },
    "E14001200": {
        "n": "Doncaster North",
        "r": -22,
        "q": 61,
    },
    "E14001201": {
        "n": "Dorking and Horley",
        "r": -43,
        "q": 59,
    },
    "E14001202": {
        "n": "Dover and Deal",
        "r": -41,
        "q": 72,
    },
    "E14001203": {
        "n": "Droitwich and Evesham",
        "r": -36,
        "q": 54,
    },
    "E14001204": {
        "n": "Dudley",
        "r": -31,
        "q": 51,
    },
    "E14001205": {
        "n": "Dulwich and West Norwood",
        "r": -42,
        "q": 63,
    },
    "E14001206": {
        "n": "Dunstable and Leighton Buzzard",
        "r": -33,
        "q": 62,
    },
    "E14001207": {
        "n": "Ealing Central and Acton",
        "r": -39,
        "q": 59,
    },
    "E14001208": {
        "n": "Ealing North",
        "r": -38,
        "q": 59,
    },
    "E14001209": {
        "n": "Ealing Southall",
        "r": -39,
        "q": 58,
    },
    "E14001210": {
        "n": "Earley and Woodley",
        "r": -36,
        "q": 56,
    },
    "E14001211": {
        "n": "Easington",
        "r": -16,
        "q": 57,
    },
    "E14001212": {
        "n": "East Grinstead and Uckfield",
        "r": -43,
        "q": 69,
    },
    "E14001213": {
        "n": "East Ham",
        "r": -38,
        "q": 67,
    },
    "E14001214": {
        "n": "East Hampshire",
        "r": -41,
        "q": 55,
    },
    "E14001215": {
        "n": "East Surrey",
        "r": -43,
        "q": 67,
    },
    "E14001216": {
        "n": "East Thanet",
        "r": -39,
        "q": 71,
    },
    "E14001217": {
        "n": "East Wiltshire",
        "r": -41,
        "q": 53,
    },
    "E14001218": {
        "n": "East Worthing and Shoreham",
        "r": -44,
        "q": 65,
    },
    "E14001219": {
        "n": "Eastbourne",
        "r": -45,
        "q": 69,
    },
    "E14001220": {
        "n": "Eastleigh",
        "r": -41,
        "q": 54,
    },
    "E14001221": {
        "n": "Edmonton and Winchmore Hill",
        "r": -36,
        "q": 64,
    },
    "E14001222": {
        "n": "Ellesmere Port and Bromborough",
        "r": -27,
        "q": 50,
    },
    "E14001223": {
        "n": "Eltham and Chislehurst",
        "r": -41,
        "q": 66,
    },
    "E14001224": {
        "n": "Ely and East Cambridgeshire",
        "r": -30,
        "q": 66,
    },
    "E14001225": {
        "n": "Enfield North",
        "r": -35,
        "q": 62,
    },
    "E14001226": {
        "n": "Epping Forest",
        "r": -35,
        "q": 67,
    },
    "E14001227": {
        "n": "Epsom and Ewell",
        "r": -43,
        "q": 60,
    },
    "E14001228": {
        "n": "Erewash",
        "r": -28,
        "q": 59,
    },
    "E14001229": {
        "n": "Erith and Thamesmead",
        "r": -40,
        "q": 67,
    },
    "E14001230": {
        "n": "Esher and Walton",
        "r": -42,
        "q": 58,
    },
    "E14001231": {
        "n": "Exeter",
        "r": -42,
        "q": 48,
    },
    "E14001232": {
        "n": "Exmouth and Exeter East",
        "r": -43,
        "q": 48,
    },
    "E14001233": {
        "n": "Fareham and Waterlooville",
        "r": -43,
        "q": 55,
    },
    "E14001234": {
        "n": "Farnham and Bordon",
        "r": -42,
        "q": 56,
    },
    "E14001235": {
        "n": "Faversham and Mid Kent",
        "r": -40,
        "q": 71,
    },
    "E14001236": {
        "n": "Feltham and Heston",
        "r": -40,
        "q": 59,
    },
    "E14001237": {
        "n": "Filton and Bradley Stoke",
        "r": -37,
        "q": 50,
    },
    "E14001238": {
        "n": "Finchley and Golders Green",
        "r": -37,
        "q": 61,
    },
    "E14001239": {
        "n": "Folkestone and Hythe",
        "r": -42,
        "q": 71,
    },
    "E14001240": {
        "n": "Forest of Dean",
        "r": -35,
        "q": 50,
    },
    "E14001241": {
        "n": "Frome and East Somerset",
        "r": -41,
        "q": 50,
    },
    "E14001242": {
        "n": "Fylde",
        "r": -19,
        "q": 51,
    },
    "E14001243": {
        "n": "Gainsborough",
        "r": -25,
        "q": 61,
    },
    "E14001244": {
        "n": "Gateshead Central and Whickham",
        "r": -15,
        "q": 56,
    },
    "E14001245": {
        "n": "Gedling",
        "r": -28,
        "q": 61,
    },
    "E14001246": {
        "n": "Gillingham and Rainham",
        "r": -40,
        "q": 70,
    },
    "E14001247": {
        "n": "Glastonbury and Somerton",
        "r": -41,
        "q": 49,
    },
    "E14001248": {
        "n": "Gloucester",
        "r": -35,
        "q": 51,
    },
    "E14001249": {
        "n": "Godalming and Ash",
        "r": -42,
        "q": 57,
    },
    "E14001250": {
        "n": "Goole and Pocklington",
        "r": -21,
        "q": 61,
    },
    "E14001251": {
        "n": "Gorton and Denton",
        "r": -24,
        "q": 55,
    },
    "E14001252": {
        "n": "Gosport",
        "r": -43,
        "q": 57,
    },
    "E14001253": {
        "n": "Grantham and Bourne",
        "r": -28,
        "q": 63,
    },
    "E14001254": {
        "n": "Gravesham",
        "r": -39,
        "q": 68,
    },
    "E14001255": {
        "n": "Great Grimsby and Cleethorpes",
        "r": -24,
        "q": 63,
    },
    "E14001256": {
        "n": "Great Yarmouth",
        "r": -27,
        "q": 67,
    },
    "E14001257": {
        "n": "Greenwich and Woolwich",
        "r": -40,
        "q": 66,
    },
    "E14001258": {
        "n": "Guildford",
        "r": -41,
        "q": 56,
    },
    "E14001259": {
        "n": "Hackney North and Stoke Newington",
        "r": -38,
        "q": 64,
    },
    "E14001260": {
        "n": "Hackney South and Shoreditch",
        "r": -39,
        "q": 64,
    },
    "E14001261": {
        "n": "Halesowen",
        "r": -33,
        "q": 51,
    },
    "E14001262": {
        "n": "Halifax",
        "r": -21,
        "q": 55,
    },
    "E14001263": {
        "n": "Hamble Valley",
        "r": -43,
        "q": 56,
    },
    "E14001264": {
        "n": "Hammersmith and Chiswick",
        "r": -39,
        "q": 60,
    },
    "E14001265": {
        "n": "Hampstead and Highgate",
        "r": -38,
        "q": 62,
    },
    "E14001266": {
        "n": "Harborough, Oadby and Wigston",
        "r": -31,
        "q": 61,
    },
    "E14001267": {
        "n": "Harlow",
        "r": -32,
        "q": 67,
    },
    "E14001268": {
        "n": "Harpenden and Berkhamsted",
        "r": -34,
        "q": 62,
    },
    "E14001269": {
        "n": "Harrogate and Knaresborough",
        "r": -18,
        "q": 59,
    },
    "E14001270": {
        "n": "Harrow East",
        "r": -37,
        "q": 60,
    },
    "E14001271": {
        "n": "Harrow West",
        "r": -37,
        "q": 59,
    },
    "E14001272": {
        "n": "Hartlepool",
        "r": -16,
        "q": 59,
    },
    "E14001273": {
        "n": "Harwich and North Essex",
        "r": -31,
        "q": 69,
    },
    "E14001274": {
        "n": "Hastings and Rye",
        "r": -43,
        "q": 70,
    },
    "E14001275": {
        "n": "Havant",
        "r": -44,
        "q": 59,
    },
    "E14001276": {
        "n": "Hayes and Harlington",
        "r": -38,
        "q": 58,
    },
    "E14001277": {
        "n": "Hazel Grove",
        "r": -25,
        "q": 55,
    },
    "E14001278": {
        "n": "Hemel Hempstead",
        "r": -34,
        "q": 64,
    },
    "E14001279": {
        "n": "Hendon",
        "r": -36,
        "q": 61,
    },
    "E14001280": {
        "n": "Henley and Thame",
        "r": -35,
        "q": 58,
    },
    "E14001281": {
        "n": "Hereford and South Herefordshire",
        "r": -34,
        "q": 51,
    },
    "E14001282": {
        "n": "Herne Bay and Sandwich",
        "r": -40,
        "q": 72,
    },
    "E14001283": {
        "n": "Hertford and Stortford",
        "r": -32,
        "q": 66,
    },
    "E14001284": {
        "n": "Hertsmere",
        "r": -34,
        "q": 66,
    },
    "E14001285": {
        "n": "Hexham",
        "r": -13,
        "q": 53,
    },
    "E14001286": {
        "n": "Heywood and Middleton North",
        "r": -20,
        "q": 54,
    },
    "E14001287": {
        "n": "High Peak",
        "r": -25,
        "q": 56,
    },
    "E14001288": {
        "n": "Hinckley and Bosworth",
        "r": -30,
        "q": 58,
    },
    "E14001289": {
        "n": "Hitchin",
        "r": -32,
        "q": 64,
    },
    "E14001290": {
        "n": "Holborn and St Pancras",
        "r": -39,
        "q": 62,
    },
    "E14001291": {
        "n": "Honiton and Sidmouth",
        "r": -43,
        "q": 49,
    },
    "E14001292": {
        "n": "Hornchurch and Upminster",
        "r": -37,
        "q": 66,
    },
    "E14001293": {
        "n": "Hornsey and Friern Barnet",
        "r": -36,
        "q": 63,
    },
    "E14001294": {
        "n": "Horsham",
        "r": -44,
        "q": 62,
    },
    "E14001295": {
        "n": "Houghton and Sunderland South",
        "r": -15,
        "q": 57,
    },
    "E14001296": {
        "n": "Hove and Portslade",
        "r": -44,
        "q": 66,
    },
    "E14001297": {
        "n": "Huddersfield",
        "r": -22,
        "q": 56,
    },
    "E14001298": {
        "n": "Huntingdon",
        "r": -31,
        "q": 63,
    },
    "E14001299": {
        "n": "Hyndburn",
        "r": -19,
        "q": 54,
    },
    "E14001300": {
        "n": "Ilford North",
        "r": -36,
        "q": 65,
    },
    "E14001301": {
        "n": "Ilford South",
        "r": -37,
        "q": 65,
    },
    "E14001302": {
        "n": "Ipswich",
        "r": -30,
        "q": 68,
    },
    "E14001303": {
        "n": "Isle of Wight East",
        "r": -45,
        "q": 54,
    },
    "E14001304": {
        "n": "Isle of Wight West",
        "r": -45,
        "q": 53,
    },
    "E14001305": {
        "n": "Islington North",
        "r": -38,
        "q": 63,
    },
    "E14001306": {
        "n": "Islington South and Finsbury",
        "r": -39,
        "q": 63,
    },
    "E14001307": {
        "n": "Jarrow and Gateshead East",
        "r": -14,
        "q": 57,
    },
    "E14001308": {
        "n": "Keighley and Ilkley",
        "r": -19,
        "q": 56,
    },
    "E14001309": {
        "n": "Kenilworth and Southam",
        "r": -34,
        "q": 56,
    },
    "E14001310": {
        "n": "Kensington and Bayswater",
        "r": -39,
        "q": 61,
    },
    "E14001311": {
        "n": "Kettering",
        "r": -30,
        "q": 61,
    },
    "E14001312": {
        "n": "Kingston and Surbiton",
        "r": -42,
        "q": 59,
    },
    "E14001313": {
        "n": "Kingston upon Hull East",
        "r": -22,
        "q": 63,
    },
    "E14001314": {
        "n": "Kingston upon Hull North and Cottingham",
        "r": -21,
        "q": 62,
    },
    "E14001315": {
        "n": "Kingston upon Hull West and Haltemprice",
        "r": -22,
        "q": 62,
    },
    "E14001316": {
        "n": "Kingswinford and South Staffordshire",
        "r": -30,
        "q": 52,
    },
    "E14001317": {
        "n": "Knowsley",
        "r": -23,
        "q": 50,
    },
    "E14001318": {
        "n": "Lancaster and Wyre",
        "r": -18,
        "q": 54,
    },
    "E14001319": {
        "n": "Leeds Central and Headingley",
        "r": -20,
        "q": 60,
    },
    "E14001320": {
        "n": "Leeds East",
        "r": -20,
        "q": 61,
    },
    "E14001321": {
        "n": "Leeds North East",
        "r": -19,
        "q": 59,
    },
    "E14001322": {
        "n": "Leeds North West",
        "r": -19,
        "q": 58,
    },
    "E14001324": {
        "n": "Leeds South West and Morley",
        "r": -21,
        "q": 58,
    },
    "E14001323": {
        "n": "Leeds South",
        "r": -21,
        "q": 59,
    },
    "E14001325": {
        "n": "Leeds West and Pudsey",
        "r": -20,
        "q": 59,
    },
    "E14001326": {
        "n": "Leicester East",
        "r": -30,
        "q": 60,
    },
    "E14001327": {
        "n": "Leicester South",
        "r": -31,
        "q": 60,
    },
    "E14001328": {
        "n": "Leicester West",
        "r": -31,
        "q": 59,
    },
    "E14001329": {
        "n": "Leigh and Atherton",
        "r": -25,
        "q": 51,
    },
    "E14001330": {
        "n": "Lewes",
        "r": -45,
        "q": 68,
    },
    "E14001331": {
        "n": "Lewisham East",
        "r": -42,
        "q": 66,
    },
    "E14001332": {
        "n": "Lewisham North",
        "r": -40,
        "q": 65,
    },
    "E14001333": {
        "n": "Lewisham West and East Dulwich",
        "r": -41,
        "q": 65,
    },
    "E14001334": {
        "n": "Leyton and Wanstead",
        "r": -37,
        "q": 64,
    },
    "E14001335": {
        "n": "Lichfield",
        "r": -29,
        "q": 56,
    },
    "E14001336": {
        "n": "Lincoln",
        "r": -25,
        "q": 62,
    },
    "E14001337": {
        "n": "Liverpool Garston",
        "r": -25,
        "q": 50,
    },
    "E14001338": {
        "n": "Liverpool Riverside",
        "r": -24,
        "q": 49,
    },
    "E14001339": {
        "n": "Liverpool Walton",
        "r": -23,
        "q": 49,
    },
    "E14001340": {
        "n": "Liverpool Wavertree",
        "r": -25,
        "q": 49,
    },
    "E14001341": {
        "n": "Liverpool West Derby",
        "r": -24,
        "q": 50,
    },
    "E14001342": {
        "n": "Loughborough",
        "r": -30,
        "q": 59,
    },
    "E14001343": {
        "n": "Louth and Horncastle",
        "r": -25,
        "q": 63,
    },
    "E14001344": {
        "n": "Lowestoft",
        "r": -28,
        "q": 68,
    },
    "E14001345": {
        "n": "Luton North",
        "r": -33,
        "q": 63,
    },
    "E14001346": {
        "n": "Luton South and South Bedfordshire",
        "r": -34,
        "q": 63,
    },
    "E14001347": {
        "n": "Macclesfield",
        "r": -26,
        "q": 56,
    },
    "E14001348": {
        "n": "Maidenhead",
        "r": -36,
        "q": 57,
    },
    "E14001349": {
        "n": "Maidstone and Malling",
        "r": -41,
        "q": 69,
    },
    "E14001350": {
        "n": "Makerfield",
        "r": -22,
        "q": 51,
    },
    "E14001351": {
        "n": "Maldon",
        "r": -33,
        "q": 69,
    },
    "E14001352": {
        "n": "Manchester Central",
        "r": -24,
        "q": 54,
    },
    "E14001353": {
        "n": "Manchester Rusholme",
        "r": -25,
        "q": 53,
    },
    "E14001354": {
        "n": "Manchester Withington",
        "r": -26,
        "q": 54,
    },
    "E14001355": {
        "n": "Mansfield",
        "r": -27,
        "q": 61,
    },
    "E14001356": {
        "n": "Melksham and Devizes",
        "r": -40,
        "q": 52,
    },
    "E14001357": {
        "n": "Melton and Syston",
        "r": -29,
        "q": 61,
    },
    "E14001358": {
        "n": "Meriden and Solihull East",
        "r": -33,
        "q": 55,
    },
    "E14001359": {
        "n": "Mid Bedfordshire",
        "r": -32,
        "q": 62,
    },
    "E14001360": {
        "n": "Mid Buckinghamshire",
        "r": -35,
        "q": 59,
    },
    "E14001361": {
        "n": "Mid Cheshire",
        "r": -27,
        "q": 52,
    },
    "E14001362": {
        "n": "Mid Derbyshire",
        "r": -27,
        "q": 57,
    },
    "E14001363": {
        "n": "Mid Dorset and North Poole",
        "r": -43,
        "q": 50,
    },
    "E14001364": {
        "n": "Mid Leicestershire",
        "r": -31,
        "q": 58,
    },
    "E14001365": {
        "n": "Mid Norfolk",
        "r": -28,
        "q": 65,
    },
    "E14001366": {
        "n": "Mid Sussex",
        "r": -43,
        "q": 68,
    },
    "E14001367": {
        "n": "Middlesbrough and Thornaby East",
        "r": -17,
        "q": 57,
    },
    "E14001368": {
        "n": "Middlesbrough South and East Cleveland",
        "r": -17,
        "q": 59,
    },
    "E14001369": {
        "n": "Milton Keynes Central",
        "r": -34,
        "q": 61,
    },
    "E14001370": {
        "n": "Milton Keynes North",
        "r": -33,
        "q": 61,
    },
    "E14001371": {
        "n": "Mitcham and Morden",
        "r": -43,
        "q": 61,
    },
    "E14001372": {
        "n": "Morecambe and Lunesdale",
        "r": -17,
        "q": 54,
    },
    "E14001373": {
        "n": "New Forest East",
        "r": -43,
        "q": 54,
    },
    "E14001374": {
        "n": "New Forest West",
        "r": -43,
        "q": 53,
    },
    "E14001375": {
        "n": "Newark",
        "r": -26,
        "q": 62,
    },
    "E14001376": {
        "n": "Newbury",
        "r": -37,
        "q": 54,
    },
    "E14001377": {
        "n": "Newcastle upon Tyne Central and West",
        "r": -13,
        "q": 54,
    },
    "E14001378": {
        "n": "Newcastle upon Tyne East and Wallsend",
        "r": -14,
        "q": 56,
    },
    "E14001379": {
        "n": "Newcastle upon Tyne North",
        "r": -13,
        "q": 55,
    },
    "E14001380": {
        "n": "Newcastle-under-Lyme",
        "r": -28,
        "q": 52,
    },
    "E14001381": {
        "n": "Newton Abbot",
        "r": -43,
        "q": 47,
    },
    "E14001382": {
        "n": "Newton Aycliffe and Spennymoor",
        "r": -16,
        "q": 56,
    },
    "E14001383": {
        "n": "Normanton and Hemsworth",
        "r": -23,
        "q": 59,
    },
    "E14001384": {
        "n": "North Bedfordshire",
        "r": -31,
        "q": 62,
    },
    "E14001385": {
        "n": "North Cornwall",
        "r": -43,
        "q": 45,
    },
    "E14001386": {
        "n": "North Cotswolds",
        "r": -37,
        "q": 53,
    },
    "E14001387": {
        "n": "North Devon",
        "r": -41,
        "q": 46,
    },
    "E14001388": {
        "n": "North Dorset",
        "r": -42,
        "q": 51,
    },
    "E14001389": {
        "n": "North Durham",
        "r": -15,
        "q": 54,
    },
    "E14001390": {
        "n": "North East Cambridgeshire",
        "r": -29,
        "q": 64,
    },
    "E14001391": {
        "n": "North East Derbyshire",
        "r": -26,
        "q": 58,
    },
    "E14001392": {
        "n": "North East Hampshire",
        "r": -38,
        "q": 56,
    },
    "E14001393": {
        "n": "North East Hertfordshire",
        "r": -32,
        "q": 65,
    },
    "E14001394": {
        "n": "North East Somerset and Hanham",
        "r": -39,
        "q": 50,
    },
    "E14001395": {
        "n": "North Herefordshire",
        "r": -34,
        "q": 52,
    },
    "E14001396": {
        "n": "North Norfolk",
        "r": -27,
        "q": 65,
    },
    "E14001397": {
        "n": "North Northumberland",
        "r": -12,
        "q": 54,
    },
    "E14001398": {
        "n": "North Shropshire",
        "r": -29,
        "q": 50,
    },
    "E14001399": {
        "n": "North Somerset",
        "r": -39,
        "q": 49,
    },
    "E14001400": {
        "n": "North Warwickshire and Bedworth",
        "r": -32,
        "q": 57,
    },
    "E14001401": {
        "n": "North West Cambridgeshire",
        "r": -30,
        "q": 64,
    },
    "E14001402": {
        "n": "North West Essex",
        "r": -31,
        "q": 66,
    },
    "E14001403": {
        "n": "North West Hampshire",
        "r": -39,
        "q": 54,
    },
    "E14001404": {
        "n": "North West Leicestershire",
        "r": -29,
        "q": 58,
    },
    "E14001405": {
        "n": "North West Norfolk",
        "r": -28,
        "q": 64,
    },
    "E14001406": {
        "n": "Northampton North",
        "r": -32,
        "q": 61,
    },
    "E14001407": {
        "n": "Northampton South",
        "r": -33,
        "q": 60,
    },
    "E14001408": {
        "n": "Norwich North",
        "r": -28,
        "q": 66,
    },
    "E14001409": {
        "n": "Norwich South",
        "r": -29,
        "q": 66,
    },
    "E14001410": {
        "n": "Nottingham East",
        "r": -29,
        "q": 60,
    },
    "E14001411": {
        "n": "Nottingham North and Kimberley",
        "r": -28,
        "q": 60,
    },
    "E14001412": {
        "n": "Nottingham South",
        "r": -29,
        "q": 59,
    },
    "E14001413": {
        "n": "Nuneaton",
        "r": -31,
        "q": 57,
    },
    "E14001414": {
        "n": "Old Bexley and Sidcup",
        "r": -41,
        "q": 67,
    },
    "E14001415": {
        "n": "Oldham East and Saddleworth",
        "r": -22,
        "q": 55,
    },
    "E14001416": {
        "n": "Oldham West, Chadderton and Royton",
        "r": -22,
        "q": 54,
    },
    "E14001417": {
        "n": "Orpington",
        "r": -43,
        "q": 66,
    },
    "E14001418": {
        "n": "Ossett and Denby Dale",
        "r": -22,
        "q": 58,
    },
    "E14001419": {
        "n": "Oxford East",
        "r": -34,
        "q": 58,
    },
    "E14001420": {
        "n": "Oxford West and Abingdon",
        "r": -35,
        "q": 57,
    },
    "E14001421": {
        "n": "Peckham",
        "r": -41,
        "q": 64,
    },
    "E14001422": {
        "n": "Pendle and Clitheroe",
        "r": -18,
        "q": 56,
    },
    "E14001423": {
        "n": "Penistone and Stocksbridge",
        "r": -23,
        "q": 56,
    },
    "E14001424": {
        "n": "Penrith and Solway",
        "r": -15,
        "q": 52,
    },
    "E14001425": {
        "n": "Peterborough",
        "r": -29,
        "q": 63,
    },
    "E14001426": {
        "n": "Plymouth Moor View",
        "r": -43,
        "q": 46,
    },
    "E14001427": {
        "n": "Plymouth Sutton and Devonport",
        "r": -44,
        "q": 47,
    },
    "E14001428": {
        "n": "Pontefract, Castleford and Knottingley",
        "r": -22,
        "q": 60,
    },
    "E14001429": {
        "n": "Poole",
        "r": -43,
        "q": 51,
    },
    "E14001430": {
        "n": "Poplar and Limehouse",
        "r": -39,
        "q": 66,
    },
    "E14001431": {
        "n": "Portsmouth North",
        "r": -43,
        "q": 58,
    },
    "E14001432": {
        "n": "Portsmouth South",
        "r": -44,
        "q": 58,
    },
    "E14001433": {
        "n": "Preston",
        "r": -19,
        "q": 52,
    },
    "E14001434": {
        "n": "Putney",
        "r": -41,
        "q": 61,
    },
    "E14001435": {
        "n": "Queen's Park and Maida Vale",
        "r": -40,
        "q": 62,
    },
    "E14001436": {
        "n": "Rawmarsh and Conisbrough",
        "r": -24,
        "q": 60,
    },
    "E14001437": {
        "n": "Rayleigh and Wickford",
        "r": -34,
        "q": 68,
    },
    "E14001438": {
        "n": "Reading Central",
        "r": -37,
        "q": 55,
    },
    "E14001439": {
        "n": "Reading West and Mid Berkshire",
        "r": -36,
        "q": 55,
    },
    "E14001440": {
        "n": "Redcar",
        "r": -17,
        "q": 58,
    },
    "E14001441": {
        "n": "Redditch",
        "r": -35,
        "q": 53,
    },
    "E14001442": {
        "n": "Reigate",
        "r": -44,
        "q": 68,
    },
    "E14001443": {
        "n": "Ribble Valley",
        "r": -18,
        "q": 55,
    },
    "E14001444": {
        "n": "Richmond and Northallerton",
        "r": -18,
        "q": 57,
    },
    "E14001445": {
        "n": "Richmond Park",
        "r": -41,
        "q": 59,
    },
    "E14001446": {
        "n": "Rochdale",
        "r": -21,
        "q": 54,
    },
    "E14001447": {
        "n": "Rochester and Strood",
        "r": -39,
        "q": 69,
    },
    "E14001448": {
        "n": "Romford",
        "r": -36,
        "q": 66,
    },
    "E14001449": {
        "n": "Romsey and Southampton North",
        "r": -40,
        "q": 54,
    },
    "E14001450": {
        "n": "Rossendale and Darwen",
        "r": -20,
        "q": 55,
    },
    "E14001451": {
        "n": "Rother Valley",
        "r": -25,
        "q": 60,
    },
    "E14001452": {
        "n": "Rotherham",
        "r": -24,
        "q": 59,
    },
    "E14001453": {
        "n": "Rugby",
        "r": -32,
        "q": 58,
    },
    "E14001454": {
        "n": "Ruislip, Northwood and Pinner",
        "r": -36,
        "q": 60,
    },
    "E14001455": {
        "n": "Runcorn and Helsby",
        "r": -28,
        "q": 51,
    },
    "E14001456": {
        "n": "Runnymede and Weybridge",
        "r": -41,
        "q": 57,
    },
    "E14001457": {
        "n": "Rushcliffe",
        "r": -28,
        "q": 62,
    },
    "E14001458": {
        "n": "Rutland and Stamford",
        "r": -29,
        "q": 62,
    },
    "E14001459": {
        "n": "Salford",
        "r": -24,
        "q": 53,
    },
    "E14001460": {
        "n": "Salisbury",
        "r": -41,
        "q": 52,
    },
    "E14001461": {
        "n": "Scarborough and Whitby",
        "r": -19,
        "q": 61,
    },
    "E14001462": {
        "n": "Scunthorpe",
        "r": -24,
        "q": 61,
    },
    "E14001463": {
        "n": "Sefton Central",
        "r": -20,
        "q": 50,
    },
    "E14001464": {
        "n": "Selby",
        "r": -21,
        "q": 60,
    },
    "E14001465": {
        "n": "Sevenoaks",
        "r": -42,
        "q": 68,
    },
    "E14001466": {
        "n": "Sheffield Brightside and Hillsborough",
        "r": -24,
        "q": 58,
    },
    "E14001467": {
        "n": "Sheffield Central",
        "r": -25,
        "q": 58,
    },
    "E14001468": {
        "n": "Sheffield Hallam",
        "r": -24,
        "q": 57,
    },
    "E14001469": {
        "n": "Sheffield Heeley",
        "r": -25,
        "q": 57,
    },
    "E14001470": {
        "n": "Sheffield South East",
        "r": -25,
        "q": 59,
    },
    "E14001471": {
        "n": "Sherwood Forest",
        "r": -27,
        "q": 62,
    },
    "E14001472": {
        "n": "Shipley",
        "r": -19,
        "q": 57,
    },
    "E14001473": {
        "n": "Shrewsbury",
        "r": -30,
        "q": 51,
    },
    "E14001474": {
        "n": "Sittingbourne and Sheppey",
        "r": -39,
        "q": 70,
    },
    "E14001475": {
        "n": "Skipton and Ripon",
        "r": -18,
        "q": 58,
    },
    "E14001476": {
        "n": "Sleaford and North Hykeham",
        "r": -26,
        "q": 63,
    },
    "E14001477": {
        "n": "Slough",
        "r": -37,
        "q": 56,
    },
    "E14001478": {
        "n": "Smethwick",
        "r": -32,
        "q": 53,
    },
    "E14001479": {
        "n": "Solihull West and Shirley",
        "r": -34,
        "q": 55,
    },
    "E14001480": {
        "n": "South Basildon and East Thurrock",
        "r": -36,
        "q": 68,
    },
    "E14001481": {
        "n": "South Cambridgeshire",
        "r": -31,
        "q": 65,
    },
    "E14001482": {
        "n": "South Cotswolds",
        "r": -38,
        "q": 53,
    },
    "E14001483": {
        "n": "South Derbyshire",
        "r": -29,
        "q": 57,
    },
    "E14001484": {
        "n": "South Devon",
        "r": -45,
        "q": 48,
    },
    "E14001485": {
        "n": "South Dorset",
        "r": -44,
        "q": 51,
    },
    "E14001486": {
        "n": "South East Cornwall",
        "r": -44,
        "q": 46,
    },
    "E14001487": {
        "n": "South Holland and The Deepings",
        "r": -27,
        "q": 63,
    },
    "E14001488": {
        "n": "South Leicestershire",
        "r": -32,
        "q": 59,
    },
    "E14001489": {
        "n": "South Norfolk",
        "r": -29,
        "q": 67,
    },
    "E14001490": {
        "n": "South Northamptonshire",
        "r": -33,
        "q": 59,
    },
    "E14001491": {
        "n": "South Ribble",
        "r": -20,
        "q": 52,
    },
    "E14001492": {
        "n": "South Shields",
        "r": -14,
        "q": 58,
    },
    "E14001493": {
        "n": "South Shropshire",
        "r": -31,
        "q": 50,
    },
    "E14001494": {
        "n": "South Suffolk",
        "r": -30,
        "q": 69,
    },
    "E14001495": {
        "n": "South West Devon",
        "r": -45,
        "q": 47,
    },
    "E14001496": {
        "n": "South West Hertfordshire",
        "r": -35,
        "q": 61,
    },
    "E14001497": {
        "n": "South West Norfolk",
        "r": -29,
        "q": 65,
    },
    "E14001498": {
        "n": "South West Wiltshire",
        "r": -41,
        "q": 51,
    },
    "E14001499": {
        "n": "Southampton Itchen",
        "r": -42,
        "q": 55,
    },
    "E14001500": {
        "n": "Southampton Test",
        "r": -42,
        "q": 54,
    },
    "E14001501": {
        "n": "Southend East and Rochford",
        "r": -34,
        "q": 69,
    },
    "E14001502": {
        "n": "Southend West and Leigh",
        "r": -35,
        "q": 68,
    },
    "E14001503": {
        "n": "Southgate and Wood Green",
        "r": -35,
        "q": 63,
    },
    "E14001504": {
        "n": "Southport",
        "r": -19,
        "q": 50,
    },
    "E14001505": {
        "n": "Spelthorne",
        "r": -40,
        "q": 58,
    },
    "E14001506": {
        "n": "Spen Valley",
        "r": -21,
        "q": 57,
    },
    "E14001507": {
        "n": "St Albans",
        "r": -34,
        "q": 65,
    },
    "E14001508": {
        "n": "St Austell and Newquay",
        "r": -44,
        "q": 45,
    },
    "E14001509": {
        "n": "St Helens North",
        "r": -21,
        "q": 50,
    },
    "E14001510": {
        "n": "St Helens South and Whiston",
        "r": -22,
        "q": 50,
    },
    "E14001511": {
        "n": "St Ives",
        "r": -46,
        "q": 43,
    },
    "E14001512": {
        "n": "St Neots and Mid Cambridgeshire",
        "r": -31,
        "q": 64,
    },
    "E14001513": {
        "n": "Stafford",
        "r": -28,
        "q": 54,
    },
    "E14001514": {
        "n": "Staffordshire Moorlands",
        "r": -27,
        "q": 56,
    },
    "E14001515": {
        "n": "Stalybridge and Hyde",
        "r": -24,
        "q": 56,
    },
    "E14001516": {
        "n": "Stevenage",
        "r": -33,
        "q": 64,
    },
    "E14001517": {
        "n": "Stockport",
        "r": -25,
        "q": 54,
    },
    "E14001518": {
        "n": "Stockton North",
        "r": -16,
        "q": 58,
    },
    "E14001519": {
        "n": "Stockton West",
        "r": -17,
        "q": 56,
    },
    "E14001520": {
        "n": "Stoke-on-Trent Central",
        "r": -28,
        "q": 55,
    },
    "E14001521": {
        "n": "Stoke-on-Trent North",
        "r": -27,
        "q": 55,
    },
    "E14001522": {
        "n": "Stoke-on-Trent South",
        "r": -29,
        "q": 55,
    },
    "E14001523": {
        "n": "Stone, Great Wyrley and Penkridge",
        "r": -28,
        "q": 53,
    },
    "E14001524": {
        "n": "Stourbridge",
        "r": -32,
        "q": 51,
    },
    "E14001525": {
        "n": "Stratford and Bow",
        "r": -38,
        "q": 65,
    },
    "E14001526": {
        "n": "Stratford-on-Avon",
        "r": -35,
        "q": 54,
    },
    "E14001527": {
        "n": "Streatham and Croydon North",
        "r": -42,
        "q": 64,
    },
    "E14001528": {
        "n": "Stretford and Urmston",
        "r": -24,
        "q": 52,
    },
    "E14001529": {
        "n": "Stroud",
        "r": -37,
        "q": 52,
    },
    "E14001530": {
        "n": "Suffolk Coastal",
        "r": -29,
        "q": 69,
    },
    "E14001531": {
        "n": "Sunderland Central",
        "r": -15,
        "q": 58,
    },
    "E14001532": {
        "n": "Surrey Heath",
        "r": -39,
        "q": 57,
    },
    "E14001533": {
        "n": "Sussex Weald",
        "r": -42,
        "q": 70,
    },
    "E14001534": {
        "n": "Sutton and Cheam",
        "r": -42,
        "q": 60,
    },
    "E14001535": {
        "n": "Sutton Coldfield",
        "r": -31,
        "q": 56,
    },
    "E14001536": {
        "n": "Swindon North",
        "r": -39,
        "q": 53,
    },
    "E14001537": {
        "n": "Swindon South",
        "r": -40,
        "q": 53,
    },
    "E14001538": {
        "n": "Tamworth",
        "r": -30,
        "q": 57,
    },
    "E14001539": {
        "n": "Tatton",
        "r": -26,
        "q": 52,
    },
    "E14001540": {
        "n": "Taunton and Wellington",
        "r": -42,
        "q": 49,
    },
    "E14001541": {
        "n": "Telford",
        "r": -29,
        "q": 52,
    },
    "E14001542": {
        "n": "Tewkesbury",
        "r": -36,
        "q": 53,
    },
    "E14001543": {
        "n": "The Wrekin",
        "r": -29,
        "q": 51,
    },
    "E14001544": {
        "n": "Thirsk and Malton",
        "r": -18,
        "q": 60,
    },
    "E14001545": {
        "n": "Thornbury and Yate",
        "r": -36,
        "q": 51,
    },
    "E14001546": {
        "n": "Thurrock",
        "r": -36,
        "q": 67,
    },
    "E14001547": {
        "n": "Tipton and Wednesbury",
        "r": -31,
        "q": 52,
    },
    "E14001548": {
        "n": "Tiverton and Minehead",
        "r": -41,
        "q": 47,
    },
    "E14001549": {
        "n": "Tonbridge",
        "r": -41,
        "q": 68,
    },
    "E14001550": {
        "n": "Tooting",
        "r": -42,
        "q": 61,
    },
    "E14001551": {
        "n": "Torbay",
        "r": -44,
        "q": 48,
    },
    "E14001552": {
        "n": "Torridge and Tavistock",
        "r": -42,
        "q": 46,
    },
    "E14001553": {
        "n": "Tottenham",
        "r": -37,
        "q": 62,
    },
    "E14001554": {
        "n": "Truro and Falmouth",
        "r": -45,
        "q": 44,
    },
    "E14001555": {
        "n": "Tunbridge Wells",
        "r": -42,
        "q": 69,
    },
    "E14001556": {
        "n": "Twickenham",
        "r": -41,
        "q": 58,
    },
    "E14001557": {
        "n": "Tynemouth",
        "r": -13,
        "q": 56,
    },
    "E14001558": {
        "n": "Uxbridge and South Ruislip",
        "r": -37,
        "q": 58,
    },
    "E14001559": {
        "n": "Vauxhall and Camberwell Green",
        "r": -41,
        "q": 63,
    },
    "E14001560": {
        "n": "Wakefield and Rothwell",
        "r": -22,
        "q": 59,
    },
    "E14001561": {
        "n": "Wallasey",
        "r": -27,
        "q": 48,
    },
    "E14001562": {
        "n": "Walsall and Bloxwich",
        "r": -30,
        "q": 55,
    },
    "E14001563": {
        "n": "Walthamstow",
        "r": -37,
        "q": 63,
    },
    "E14001564": {
        "n": "Warrington North",
        "r": -23,
        "q": 51,
    },
    "E14001565": {
        "n": "Warrington South",
        "r": -24,
        "q": 51,
    },
    "E14001566": {
        "n": "Warwick and Leamington",
        "r": -35,
        "q": 55,
    },
    "E14001567": {
        "n": "Washington and Gateshead South",
        "r": -15,
        "q": 55,
    },
    "E14001568": {
        "n": "Watford",
        "r": -35,
        "q": 65,
    },
    "E14001569": {
        "n": "Waveney Valley",
        "r": -28,
        "q": 67,
    },
    "E14001570": {
        "n": "Weald of Kent",
        "r": -41,
        "q": 70,
    },
    "E14001571": {
        "n": "Wellingborough and Rushden",
        "r": -30,
        "q": 63,
    },
    "E14001572": {
        "n": "Wells and Mendip Hills",
        "r": -40,
        "q": 50,
    },
    "E14001573": {
        "n": "Welwyn Hatfield",
        "r": -33,
        "q": 65,
    },
    "E14001574": {
        "n": "West Bromwich",
        "r": -32,
        "q": 52,
    },
    "E14001575": {
        "n": "West Dorset",
        "r": -44,
        "q": 50,
    },
    "E14001576": {
        "n": "West Ham and Beckton",
        "r": -38,
        "q": 66,
    },
    "E14001577": {
        "n": "West Lancashire",
        "r": -21,
        "q": 49,
    },
    "E14001578": {
        "n": "West Suffolk",
        "r": -30,
        "q": 67,
    },
    "E14001579": {
        "n": "West Worcestershire",
        "r": -35,
        "q": 52,
    },
    "E14001580": {
        "n": "Westmorland and Lonsdale",
        "r": -15,
        "q": 53,
    },
    "E14001581": {
        "n": "Weston-super-Mare",
        "r": -40,
        "q": 49,
    },
    "E14001582": {
        "n": "Wetherby and Easingwold",
        "r": -20,
        "q": 62,
    },
    "E14001583": {
        "n": "Whitehaven and Workington",
        "r": -16,
        "q": 53,
    },
    "E14001584": {
        "n": "Widnes and Halewood",
        "r": -26,
        "q": 51,
    },
    "E14001585": {
        "n": "Wigan",
        "r": -20,
        "q": 51,
    },
    "E14001586": {
        "n": "Wimbledon",
        "r": -41,
        "q": 60,
    },
    "E14001587": {
        "n": "Winchester",
        "r": -40,
        "q": 55,
    },
    "E14001588": {
        "n": "Windsor",
        "r": -38,
        "q": 57,
    },
    "E14001589": {
        "n": "Wirral West",
        "r": -28,
        "q": 49,
    },
    "E14001590": {
        "n": "Witham",
        "r": -33,
        "q": 68,
    },
    "E14001591": {
        "n": "Witney",
        "r": -35,
        "q": 56,
    },
    "E14001592": {
        "n": "Woking",
        "r": -40,
        "q": 57,
    },
    "E14001593": {
        "n": "Wokingham",
        "r": -38,
        "q": 55,
    },
    "E14001594": {
        "n": "Wolverhampton North East",
        "r": -29,
        "q": 53,
    },
    "E14001595": {
        "n": "Wolverhampton South East",
        "r": -30,
        "q": 54,
    },
    "E14001596": {
        "n": "Wolverhampton West",
        "r": -30,
        "q": 53,
    },
    "E14001597": {
        "n": "Worcester",
        "r": -34,
        "q": 53,
    },
    "E14001598": {
        "n": "Worsley and Eccles",
        "r": -23,
        "q": 52,
    },
    "E14001599": {
        "n": "Worthing West",
        "r": -44,
        "q": 64,
    },
    "E14001600": {
        "n": "Wycombe",
        "r": -36,
        "q": 58,
    },
    "E14001601": {
        "n": "Wyre Forest",
        "r": -33,
        "q": 50,
    },
    "E14001602": {
        "n": "Wythenshawe and Sale East",
        "r": -26,
        "q": 53,
    },
    "E14001603": {
        "n": "Yeovil",
        "r": -42,
        "q": 50,
    },
    "E14001604": {
        "n": "York Central",
        "r": -19,
        "q": 60,
    },
    "E14001605": {
        "n": "York Outer",
        "r": -18,
        "q": 61,
    },
    "parl.east-antrim.2024-07-04": {
        "n": "East Antrim",
        "r": -15,
        "q": 45,
    },
    "parl.south-antrim.2024-07-04": {
        "n": "South Antrim",
        "r": -16,
        "q": 44,
    },
    "parl.lagan-valley.2024-07-04": {
        "n": "Lagan Valley",
        "r": -18,
        "q": 44,
    },
    "parl.upper-bann.2024-07-04": {
        "n": "Upper Bann",
        "r": -18,
        "q": 43,
    },
    "parl.belfast-north.2024-07-04": {
        "n": "Belfast North",
        "r": -16,
        "q": 45,
    },
    "parl.east-londonderry.2024-07-04": {
        "n": "East Londonderry",
        "r": -15,
        "q": 43,
    },
    "parl.west-tyrone.2024-07-04": {
        "n": "West Tyrone",
        "r": -16,
        "q": 42,
    },
    "parl.foyle.2024-07-04": {
        "n": "Foyle",
        "r": -15,
        "q": 42,
    },
    "parl.north-antrim.2024-07-04": {
        "n": "North Antrim",
        "r": -15,
        "q": 44,
    },
    "parl.mid-ulster.2024-07-04": {
        "n": "Mid Ulster",
        "r": -16,
        "q": 43,
    },
    "parl.fermanagh-and-south-tyrone.2024-07-04": {
        "n": "Fermanagh and South Tyrone",
        "r": -17,
        "q": 42,
    },
    "parl.south-down.2024-07-04": {
        "n": "South Down",
        "r": -18,
        "q": 46,
    },
    "parl.north-down.2024-07-04": {
        "n": "North Down",
        "r": -16,
        "q": 46,
    },
    "parl.strangford.2024-07-04": {
        "n": "Strangford",
        "r": -17,
        "q": 46,
    },
    "parl.belfast-east.2024-07-04": {
        "n": "Belfast East",
        "r": -17,
        "q": 45,
    },
    "parl.belfast-west.2024-07-04": {
        "n": "Belfast West",
        "r": -17,
        "q": 44,
    },
    "parl.belfast-south-and-mid-down.2024-07-04": {
        "n": "Belfast South and Mid Down",
        "r": -18,
        "q": 45,
    },
    "parl.newry-and-armagh.2024-07-04": {
        "n": "Newry and Armagh",
        "r": -19,
        "q": 44,
    },
    "parl.berwickshire-roxburgh-and-selkirk.2024-07-04": {
        "n": "Berwickshire, Roxburgh and Selkirk",
        "r": -12,
        "q": 53,
        "region": "S92000003",
    },
    "S14000066": {
        "n": "Arbroath and Broughty Ferry",
        "r": -5,
        "q": 52,
        "region": "S92000003",
    },
    "S14000076": {
        "n": "Dunfermline and Dollar",
        "r": -7,
        "q": 51,
        "region": "S92000003",
    },
    "S14000063": {
        "n": "Airdrie and Shotts",
        "r": -11,
        "q": 50,
        "region": "S92000003",
    },
    "S14000077": {
        "n": "East Kilbride and Strathaven",
        "r": -13,
        "q": 48,
        "region": "S92000003",
    },
    "S14000021": {
        "n": "East Renfrewshire",
        "r": -11,
        "q": 48,
        "region": "S92000003",
    },
    "S14000078": {
        "n": "Edinburgh East and Musselburgh",
        "r": -10,
        "q": 54,
        "region": "S92000003",
    },
    "S14000079": {
        "n": "Edinburgh North and Leith",
        "r": -9,
        "q": 53,
        "region": "S92000003",
    },
    "S14000081": {
        "n": "Edinburgh South West",
        "r": -10,
        "q": 52,
        "region": "S92000003",
    },
    "S14000064": {
        "n": "Alloa and Grangemouth",
        "r": -7,
        "q": 50,
        "region": "S92000003",
    },
    "S14000088": {
        "n": "Glasgow South West",
        "r": -10,
        "q": 50,
        "region": "S92000003",
    },
    "S14000093": {
        "n": "Inverclyde and Renfrewshire West",
        "r": -8,
        "q": 48,
        "region": "S92000003",
    },
    "parl.kilmarnock-and-loudoun.2024-07-04": {
        "n": "Kilmarnock and Loudoun",
        "r": -13,
        "q": 50,
        "region": "S92000003",
    },
    "S14000095": {
        "n": "Livingston",
        "r": -11,
        "q": 51,
        "region": "S92000003",
    },
    "S14000045": {
        "n": "Midlothian",
        "r": -11,
        "q": 52,
        "region": "S92000003",
    },
    "S14000099": {
        "n": "Motherwell, Wishaw and Carluke",
        "r": -12,
        "q": 52,
        "region": "S92000003",
    },
    "S14000102": {
        "n": "Paisley and Renfrewshire South",
        "r": -10,
        "q": 49,
        "region": "S92000003",
    },
    "S14000065": {
        "n": "Angus and Perthshire Glens",
        "r": -5,
        "q": 50,
        "region": "S92000003",
    },
    "S14000105": {
        "n": "Stirling and Strathallan",
        "r": -6,
        "q": 49,
        "region": "S92000003",
    },
    "S14000106": {
        "n": "West Dunbartonshire",
        "r": -7,
        "q": 48,
        "region": "S92000003",
    },
    "S14000098": {
        "n": "Moray West, Nairn and Strathspey",
        "r": -4,
        "q": 49,
        "region": "S92000003",
    },
    "S14000067": {
        "n": "Argyll, Bute and South Lochaber",
        "r": -5,
        "q": 49,
        "region": "S92000003",
    },
    "parl.west-aberdeenshire-and-kincardine.2024-07-04": {
        "n": "West Aberdeenshire and Kincardine",
        "r": -4,
        "q": 51,
        "region": "S92000003",
    },
    "S14000091": {
        "n": "Gordon and Buchan",
        "r": -4,
        "q": 50,
        "region": "S92000003",
    },
    "S14000071": {
        "n": "Cowdenbeath and Kirkcaldy",
        "r": -7,
        "q": 52,
        "region": "S92000003",
    },
    "S14000061": {
        "n": "Aberdeen South",
        "r": -4,
        "q": 52,
        "region": "S92000003",
    },
    "S14000082": {
        "n": "Edinburgh West",
        "r": -9,
        "q": 52,
        "region": "S92000003",
    },
    "S14000096": {
        "n": "Lothian East",
        "r": -11,
        "q": 53,
        "region": "S92000003",
    },
    "parl.ayr-carrick-and-cumnock.2024-07-04": {
        "n": "Ayr, Carrick and Cumnock",
        "r": -13,
        "q": 49,
        "region": "S92000003",
    },
    "parl.central-ayrshire.2024-07-04": {
        "n": "Central Ayrshire",
        "r": -12,
        "q": 48,
        "region": "S92000003",
    },
    "S14000051": {
        "n": "Orkney and Shetland",
        "r": 0,
        "q": 51,
        "region": "S92000003",
    },
    "S14000027": {
        "n": "Na h-Eileanan an Iar",
        "r": -2,
        "q": 47,
        "region": "S92000003",
    },
    "S14000048": {
        "n": "North Ayrshire and Arran",
        "r": -10,
        "q": 48,
        "region": "S92000003",
    },
    "S14000103": {
        "n": "Perth and Kinross-shire",
        "r": -5,
        "q": 51,
        "region": "S92000003",
    },
    "S14000075": {
        "n": "Dundee Central",
        "r": -6,
        "q": 50,
        "region": "S92000003",
    },
    "S14000083": {
        "n": "Falkirk",
        "r": -8,
        "q": 51,
        "region": "S92000003",
    },
    "S14000068": {
        "n": "Bathgate and Linlithgow",
        "r": -9,
        "q": 51,
        "region": "S92000003",
    },
    "S14000094": {
        "n": "Inverness, Skye and West Ross-shire",
        "r": -3,
        "q": 49,
        "region": "S92000003",
    },
    "S14000080": {
        "n": "Edinburgh South",
        "r": -10,
        "q": 53,
        "region": "S92000003",
    },
    "S14000073": {
        "n": "Dumfries and Galloway",
        "r": -13,
        "q": 51,
        "region": "S92000003",
    },
    "S14000101": {
        "n": "Paisley and Renfrewshire North",
        "r": -9,
        "q": 48,
        "region": "S92000003",
    },
    "S14000062": {
        "n": "Aberdeenshire North and Moray East",
        "r": -3,
        "q": 51,
        "region": "S92000003",
    },
    "S14000069": {
        "n": "Caithness, Sutherland and Easter Ross",
        "r": -2,
        "q": 50,
        "region": "S92000003",
    },
    "S14000084": {
        "n": "Glasgow East",
        "r": -10,
        "q": 51,
        "region": "S92000003",
    },
    "S14000097": {
        "n": "Mid Dunbartonshire",
        "r": -7,
        "q": 49,
        "region": "S92000003",
    },
    "S14000085": {
        "n": "Glasgow North",
        "r": -9,
        "q": 49,
        "region": "S92000003",
    },
    "S14000087": {
        "n": "Glasgow South",
        "r": -11,
        "q": 49,
        "region": "S92000003",
    },
    "S14000089": {
        "n": "Glasgow West",
        "r": -8,
        "q": 49,
        "region": "S92000003",
    },
    "S14000072": {
        "n": "Cumbernauld and Kirkintilloch",
        "r": -8,
        "q": 50,
        "region": "S92000003",
    },
    "S14000070": {
        "n": "Coatbridge and Bellshill",
        "r": -12,
        "q": 50,
        "region": "S92000003",
    },
    "S14000092": {
        "n": "Hamilton and Clyde Valley",
        "r": -12,
        "q": 51,
        "region": "S92000003",
    },
    "S14000104": {
        "n": "Rutherglen",
        "r": -12,
        "q": 49,
        "region": "S92000003",
    },
    "S14000086": {
        "n": "Glasgow North East",
        "r": -9,
        "q": 50,
        "region": "S92000003",
    },
    "S14000060": {
        "n": "Aberdeen North",
        "r": -3,
        "q": 52,
        "region": "S92000003",
    },
    "S14000074": {
        "n": "Dumfriesshire, Clydesdale and Tweeddale",
        "r": -13,
        "q": 52,
        "region": "S92000003",
    },
    "S14000100": {
        "n": "North East Fife",
        "r": -6,
        "q": 51,
        "region": "S92000003",
    },
    "S14000090": {
        "n": "Glenrothes and Mid Fife",
        "r": -6,
        "q": 52,
        "region": "S92000003",
    },
    "W07000081": {
        "n": "Aberafan Maesteg",
        "r": -36,
        "q": 46,
        "region": "W92000004",
    },
    "W07000082": {
        "n": "Alyn and Deeside",
        "r": -29,
        "q": 49,
        "region": "W92000004",
    },
    "W07000083": {
        "n": "Bangor Aberconwy",
        "r": -31,
        "q": 47,
        "region": "W92000004",
    },
    "W07000084": {
        "n": "Blaenau Gwent and Rhymney",
        "r": -33,
        "q": 49,
        "region": "W92000004",
    },
    "W07000085": {
        "n": "Brecon, Radnor and Cwm Tawe",
        "r": -32,
        "q": 50,
        "region": "W92000004",
    },
    "W07000086": {
        "n": "Bridgend",
        "r": -37,
        "q": 46,
        "region": "W92000004",
    },
    "W07000087": {
        "n": "Caerfyrddin",
        "r": -32,
        "q": 49,
        "region": "W92000004",
    },
    "W07000088": {
        "n": "Caerphilly",
        "r": -35,
        "q": 49,
        "region": "W92000004",
    },
    "W07000089": {
        "n": "Cardiff East",
        "r": -37,
        "q": 48,
        "region": "W92000004",
    },
    "W07000090": {
        "n": "Cardiff North",
        "r": -36,
        "q": 48,
        "region": "W92000004",
    },
    "W07000091": {
        "n": "Cardiff South and Penarth",
        "r": -38,
        "q": 48,
        "region": "W92000004",
    },
    "W07000092": {
        "n": "Cardiff West",
        "r": -37,
        "q": 47,
        "region": "W92000004",
    },
    "W07000093": {
        "n": "Ceredigion Preseli",
        "r": -34,
        "q": 48,
        "region": "W92000004",
    },
    "W07000094": {
        "n": "Clwyd East",
        "r": -30,
        "q": 49,
        "region": "W92000004",
    },
    "W07000095": {
        "n": "Clwyd North",
        "r": -30,
        "q": 48,
        "region": "W92000004",
    },
    "W07000096": {
        "n": "Dwyfor Meirionnydd",
        "r": -31,
        "q": 48,
        "region": "W92000004",
    },
    "W07000097": {
        "n": "Gower",
        "r": -37,
        "q": 44,
        "region": "W92000004",
    },
    "W07000098": {
        "n": "Llanelli",
        "r": -36,
        "q": 45,
        "region": "W92000004",
    },
    "W07000099": {
        "n": "Merthyr Tydfil and Aberdare",
        "r": -34,
        "q": 49,
        "region": "W92000004",
    },
    "W07000100": {
        "n": "Mid and South Pembrokeshire",
        "r": -36,
        "q": 44,
        "region": "W92000004",
    },
    "W07000101": {
        "n": "Monmouthshire",
        "r": -36,
        "q": 50,
        "region": "W92000004",
    },
    "W07000102": {
        "n": "Montgomeryshire and Glyndŵr",
        "r": -31,
        "q": 49,
        "region": "W92000004",
    },
    "W07000103": {
        "n": "Neath and Swansea East",
        "r": -35,
        "q": 47,
        "region": "W92000004",
    },
    "W07000104": {
        "n": "Newport East",
        "r": -37,
        "q": 49,
        "region": "W92000004",
    },
    "W07000105": {
        "n": "Newport West and Islwyn",
        "r": -36,
        "q": 49,
        "region": "W92000004",
    },
    "W07000106": {
        "n": "Pontypridd",
        "r": -35,
        "q": 48,
        "region": "W92000004",
    },
    "W07000107": {
        "n": "Rhondda and Ogmore",
        "r": -36,
        "q": 47,
        "region": "W92000004",
    },
    "W07000108": {
        "n": "Swansea West",
        "r": -37,
        "q": 45,
        "region": "W92000004",
    },
    "W07000109": {
        "n": "Torfaen",
        "r": -34,
        "q": 50,
        "region": "W92000004",
    },
    "W07000110": {
        "n": "Vale of Glamorgan",
        "r": -38,
        "q": 47,
        "region": "W92000004",
    },
    "W07000111": {
        "n": "Wrexham",
        "r": -30,
        "q": 50,
        "region": "W92000004",
    },
    "W07000112": {
        "n": "Ynys Môn",
        "r": -29,
        "q": 46,
        "region": "W92000004",
    },
    "E14001063": {
        "n": "Aldershot",
        "r": -40,
        "q": 56,
    },
    "E14001064": {
        "n": "Aldridge-Brownhills",
        "r": -30,
        "q": 56,
    },
    "E14001065": {
        "n": "Altrincham and Sale West",
        "r": -25,
        "q": 52,
    },
    "E14001066": {
        "n": "Amber Valley",
        "r": -27,
        "q": 58,
    },
    "E14001067": {
        "n": "Arundel and South Downs",
        "r": -44,
        "q": 61,
    },
    "E14001068": {
        "n": "Ashfield",
        "r": -27,
        "q": 60,
    },
    "E14001069": {
        "n": "Ashford",
        "r": -42,
        "q": 72,
    },
    "E14001070": {
        "n": "Ashton-under-Lyne",
        "r": -23,
        "q": 54,
    },
    "E14001071": {
        "n": "Aylesbury",
        "r": -35,
        "q": 60,
    },
    "E14001072": {
        "n": "Banbury",
        "r": -33,
        "q": 58,
    },
    "E14001073": {
        "n": "Barking",
        "r": -38,
        "q": 68,
    },
    "E14001076": {
        "n": "Barrow and Furness",
        "r": -16,
        "q": 54,
    },
    "E14001077": {
        "n": "Basildon and Billericay",
        "r": -34,
        "q": 67,
    },
    "E14001078": {
        "n": "Basingstoke",
        "r": -39,
        "q": 55,
    },
    "E14001079": {
        "n": "Bassetlaw",
        "r": -26,
        "q": 61,
    },
    "E14001080": {
        "n": "Bath",
        "r": -40,
        "q": 51,
    },
    "E14001081": {
        "n": "Battersea",
        "r": -41,
        "q": 62,
    },
    "E14001082": {
        "n": "Beaconsfield",
        "r": -37,
        "q": 57,
    },
    "E14001084": {
        "n": "Bedford",
        "r": -32,
        "q": 63,
    },
    "E14001085": {
        "n": "Bermondsey and Old Southwark",
        "r": -40,
        "q": 64,
    },
    "E14001087": {
        "n": "Beverley and Holderness",
        "r": -22,
        "q": 64,
    },
    "E14001088": {
        "n": "Bexhill and Battle",
        "r": -44,
        "q": 70,
    },
    "E14001089": {
        "n": "Bexleyheath and Crayford",
        "r": -39,
        "q": 67,
    },
    "E14001091": {
        "n": "Birkenhead",
        "r": -27,
        "q": 49,
    },
    "E14001101": {
        "n": "Bishop Auckland",
        "r": -14,
        "q": 54,
    },
    "E14001102": {
        "n": "Blackburn",
        "r": -19,
        "q": 53,
    },
    "E14001105": {
        "n": "Blackpool South",
        "r": -18,
        "q": 52,
    },
    "E14001108": {
        "n": "Bognor Regis and Littlehampton",
        "r": -44,
        "q": 63,
    },
    "E14001109": {
        "n": "Bolsover",
        "r": -26,
        "q": 60,
    },
    "E14001110": {
        "n": "Bolton North East",
        "r": -21,
        "q": 52,
    },
    "E14001112": {
        "n": "Bolton West",
        "r": -21,
        "q": 51,
    },
    "E14001113": {
        "n": "Bootle",
        "r": -22,
        "q": 49,
    },
    "E14001114": {
        "n": "Boston and Skegness",
        "r": -26,
        "q": 64,
    },
    "E14001115": {
        "n": "Bournemouth East",
        "r": -43,
        "q": 52,
    },
    "E14001116": {
        "n": "Bournemouth West",
        "r": -42,
        "q": 52,
    },
    "E14001117": {
        "n": "Bracknell",
        "r": -39,
        "q": 56,
    },
    "E14001118": {
        "n": "Bradford East",
        "r": -20,
        "q": 58,
    },
    "E14001119": {
        "n": "Bradford South",
        "r": -21,
        "q": 56,
    },
    "E14001120": {
        "n": "Bradford West",
        "r": -20,
        "q": 57,
    },
    "E14001121": {
        "n": "Braintree",
        "r": -31,
        "q": 67,
    },
    "E14001124": {
        "n": "Brentford and Isleworth",
        "r": -40,
        "q": 60,
    },
    "E14001125": {
        "n": "Brentwood and Ongar",
        "r": -33,
        "q": 66,
    },
    "E14001132": {
        "n": "Bristol East",
        "r": -38,
        "q": 52,
    },
}

party_colour_map = {
    "PP53": "#E4003B",  # Lab
    "joint-party53-119": "#E4003B",  # Lab/Co-op
    "PP52": "#0087DC",  # Con
    "PP90": "#FAA61A",  # LibDem
    "PP7931": "#00B1DA",  # Reform
    "PP102": "#FDF38E",  # SNP
    "PP130": "#00B140",  # Scottish Green Party
    "PP12700": "#005EB8",  # Alba
    "PP63": "#00643B",  # Green
    "PP77": "#005b54",  # Plaid Cymru
    "PP70": "#D46A4C",  # Democratic Unionist Party (DUP)
    "PP39": "#00623F",  # Sinn Féin
    "PP103": "#F6CB2F",  # Alliance Party of Northern Ireland
    "PP55": "#2AA82C",  # Social Democratic and Labour Party (SDLP)
    "PP83": "#48A5EE",  # Ulster Unionist Party (UUP)
}


@register.filter(name="constituency_to_hex_row")
def constituency_to_hex_row(ballot):
    ynr_id = ballot.post.ynr_id
    ballot_id = ballot.ballot_paper_id
    if ynr_id.startswith("gss:"):
        ballot_id = ynr_id[4:]

    data = gss_to_hex.get(ballot_id, gss_to_hex.get(ballot.ballot_paper_id))
    if ballot.elected_person_post_id:
        data["colour"] = party_colour_map.get(
            ballot.elected_person_post_party, "#403F41"
        )
        data["party_name"] = ballot.elected_person_post_party_name
    else:
        data["colour"] = "rgba(64, 63, 65, 0.2)"
        data["party_name"] = ""
    return mark_safe(f""""{ballot_id}": {data},""")
