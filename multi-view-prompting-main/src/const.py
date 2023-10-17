import json
from pathlib import Path
senttag2opinion = {'pos': 'great', 'neg': 'bad', 'neu': 'ok'}
sentword2opinion = {'positive': 'great', 'negative': 'bad', 'neutral': 'ok'}

rest_aspect_cate_list = [
    'location general', 'food prices', 'food quality', 'food general',
    'ambience general', 'service general', 'restaurant prices',
    'drinks prices', 'restaurant miscellaneous', 'drinks quality',
    'drinks style_options', 'restaurant general', 'food style_options'
]

laptop_aspect_cate_list = [
    'keyboard operation_performance', 'os operation_performance',
    'out_of_scope operation_performance', 'ports general',
    'optical_drives general', 'laptop operation_performance',
    'optical_drives operation_performance', 'optical_drives usability',
    'multimedia_devices general', 'keyboard general', 'os miscellaneous',
    'software operation_performance', 'display operation_performance',
    'shipping quality', 'hard_disc quality', 'motherboard general',
    'graphics general', 'multimedia_devices connectivity', 'display general',
    'memory operation_performance', 'os design_features',
    'out_of_scope usability', 'software design_features',
    'graphics design_features', 'ports connectivity',
    'support design_features', 'display quality', 'software price',
    'shipping general', 'graphics operation_performance',
    'hard_disc miscellaneous', 'display design_features',
    'cpu operation_performance', 'mouse general', 'keyboard portability',
    'hardware price', 'support quality', 'hardware quality',
    'motherboard operation_performance', 'multimedia_devices quality',
    'battery design_features', 'mouse usability', 'os price',
    'shipping operation_performance', 'laptop quality', 'laptop portability',
    'fans&cooling general', 'battery general', 'os usability',
    'hardware usability', 'optical_drives design_features',
    'fans&cooling operation_performance', 'memory general', 'company general',
    'power_supply general', 'hardware general', 'mouse design_features',
    'software general', 'keyboard quality', 'power_supply quality',
    'software quality', 'multimedia_devices usability',
    'power_supply connectivity', 'multimedia_devices price',
    'multimedia_devices operation_performance', 'ports design_features',
    'hardware operation_performance', 'shipping price',
    'hardware design_features', 'memory usability', 'cpu quality',
    'ports quality', 'ports portability', 'motherboard quality',
    'display price', 'os quality', 'graphics usability', 'cpu design_features',
    'hard_disc general', 'hard_disc operation_performance', 'battery quality',
    'laptop usability', 'company design_features',
    'company operation_performance', 'support general', 'fans&cooling quality',
    'memory design_features', 'ports usability', 'hard_disc design_features',
    'power_supply design_features', 'keyboard miscellaneous',
    'laptop miscellaneous', 'keyboard usability', 'cpu price',
    'laptop design_features', 'keyboard price', 'warranty quality',
    'display usability', 'support price', 'cpu general',
    'out_of_scope design_features', 'out_of_scope general',
    'software usability', 'laptop general', 'warranty general',
    'company price', 'ports operation_performance',
    'power_supply operation_performance', 'keyboard design_features',
    'support operation_performance', 'hard_disc usability', 'os general',
    'company quality', 'memory quality', 'software portability',
    'fans&cooling design_features', 'multimedia_devices design_features',
    'laptop connectivity', 'battery operation_performance', 'hard_disc price',
    'laptop price'
]
phone_aspect_cate_list = ["water", "night scene mode", "dont play games", "overall UI interaction", "aftersales service of small factories", "2K LCD screen", 
    "visual impact", "bright screen", "photo experience.If", "latency", "ISO key combination", "system setting", "scan the code", "take photos", "like", "high refresh rate strategy", "low frequency",
    "battery lifetime", "taking pictures, taking pictures", "1000", "rangle", "Play the King of Glory", "120w fast charge", "threefinger screenshots", "functionality", "game experience",
    "realtime shooting", "rear", "lasts for", "Workmanship", "shooting casually", "background", "67w single cell", "capture", "positioning", "games", "motherboard", "other", "charge 55W",
    "Magnetic Cooling Back Clip", "R corner", "ultimate stable frame rate", "Samsung e3 90hz", "100 million pixel mode", "large nuclear frequency", "Qualcomm baseband", "width",
    "daytime light comparison, HDR", "consume power", "portraits", "processors", "fringe", "market feedback", "blood recovery", "baseband", "overall experience", "surging C1 chip",
    "photo taking", "charge", "global sales", "tuning", "Burning wifi and motherboard", "586", "8G memory", "else", "brush, the battery life of the 13pro can", "Take pictures", "cost effective",
    "DC", "play Honor of King", "carlife", "night vision video", "sharpening", "body", "navigating", "temperature control", "internal space", "costeffectiveness", "curved", "4g and 60hz", "bug",
    "video website", "z axis", "25W", "configuration parameters", "curved screens", "extreme image quality", "The battery life", "data", "decoration of the camera", "flexible straight screen", "battery size",
    "value preservation rate", "background management", "feel bad in hand", "glory of the king", "direct screen", "killing the backstage", "a lot of apps", "no nfc, no infrared", "single lift", "2.5D glass",
    "picture effect", "frame", "making calls", "creases", "5g", "software optimization", "play King", "telephoto", "cameras image quality", "training", "Z axis", "optimization", "movie mode", "apperance",
    "value preservation", "Periscope", "frequency bands", "take a picture", "Qualcomm chip", "small window", "5x", "side fingerprints", "recognition", "top match", "feel texture", "charging power",
    "Wechat messages", "smoothness of use", "Game", "main camera focus", "9.08 system", "RAM", "screen effect", "plastic back cover", "technology", "ultrawide angle", "screenclosing button", "Sales",
    "Optimization", "cooling", "sensitivity dial", "photoshoot", "privacy", "cost", "870", "plastic midframe", "thinness", "vpn", "core technology", "Intel baseband", "buttons", "bulge control",
    "lock screen key", "waterproof screen", "technologies", "market value", "Zeissga", "long screenshot", "ltpo", "LCD Huaxing Optoelectronics screens", "bugs than", "Night owl", "system maintenance",
    "maintenance point", "appearance", "underlying architecture", "Opening the program", "5x telephoto in the video", "exquisite feeling", "quality of workmanship", "lower limit", "camera", "chicken",
    "high load", "external sound", "Play games", "play games", "raw", "bottom layer", "fillet", "12.5 enhanced version", "bright screen fast", "contrast ratio", "shoot people", "imx686", "offline discount",
    "screen time reminds", "software quality", "Xaxis motor", "inherited design characteristics", "power", "main camera algorith", "r corner", "desktop sliding", "sales volume", "screen durability", "tune",
    "5x telephoto", "main shooter", "large curved screen", "preview", "bezel", "King of Glory", "weight", "peripherals", "778G", "fingerprint payment", "2K Samsung flexible screen", "100 million pixels",
    "extreme 90 frames", "simple vertical bar design", "comprehensive battery life", "system optimization capabilities", "patriotic marketing", "filter", "image quality", "game dispatch", "video level",
    "Zhou Dongyu arrangement", "watching hdr video", "back cover design", "gap in the back cover", "oneui", "thick", "details of the bright part", "lens quality", "optical focus", "fixed focus", "ID",
    "Photo color reproduction", "color os", "configuration of other processors", "frame drop", "adaptive high brush", "play the game", "camera optimization", "Fast charging", "takes photos", "temperature",
    "miui", "software response", "software opening speed", "r angle", "return to the factory", "Animation", "linear motor", "batteries", "singlecell", "766ois", "details", "humanization", "text messages",
    "surface", "brand influence", "rightangled sides", "image stabilization", "LCD", "stroboscopic", "pixel", "performance strategy", "to unlock", "LTPO", "hyperboloid", "hardware parameters",
    "rightangle frame", "quality of the screen", "plastic back", "Feel", "sincerity", "burning wifi", "powerdown feedback", "overall shooting experience", "materials", "Taking pictures", "module design",
    "grooving", "ultrasonic widearea fingerprints", "animations", "back fingerprint", "accessories", "dual color temperature flash", "dissipate heat", "curvature screen", "color algorith",
    "play the glory of king", "lens", "frame drops", "product strength", "subcamera", "120w fast charging head", "playability", "sensitivity control wheel", "experience quality", "controlled",
    "high brush experience", "UI optimization", "ability to shoot", "notch", "large screen", "negative one screen", "parameters", "reduced the price", "fineness of the animation", "desktop",
    "Dimensity 9000", "ease of use of the system", "display area", "macro", "battery status", "measurements", "pricing", "small dot design", "with all aspects", "recording videos", "textures",
    "System maintenance", "when shooting", "Hasselblad", "90hz", "image algorithm tuning", "folding screens", "stability", "details and colors", "product force", "keys", "screen time", "dark mode",
    "camera algorith", "word of mouth", "System optimization", "noise", "Coloros", "last LCD screen", "system animations", "priceperformance ratio", "Scheduling", "body texture", "group", "difference",
    "NFC", "body ceramic", "algorithm for taking pictures", "type", "motor experience", "playing the King", "secondly the signal", "Kirin 9000", "balanced performance power consumption", "old model",
    "closeup shots", "1080PLCD screen", "positioned", "playing King", "playing the King of Glory", "Honor of Kings", "battery health", "case", "black", "usage cycle", "big screen", "screen ratio",
    "camera module designs", "sky 920", "Samsung 1080P screen", "background improvement", "product line", "dissipates heat", "Harzu", "design logic", "slides up and down", "touch sampling rate", "8890",
    "image algorith", "bugs", "slide down", "screen flicker", "feel", "popup camera", "back cover", "shoot at night", "photo", "rear camera module", "DC lighting", "samples", "elevator", "main camera",
    "highend", "night owl", "network switching", "High Brush", "120hz", "saturation", "battery life of the game", "accumulation of heat dissipation", "daily use", "photo function", "night mode", "25W power",
    "system experience", "Samsung 2K screen", "performance mode", "MIUI13", "imaging", "little window", "100 million pixel", "daily operation", "peripheral parameters", "telephoto lenses",
    "comprehensive experience", "charging head", "not playing games", "message came", "design aesthetics", "single speaker", "imagery", "texture", "scheduling", "jbl four speakers", "cost performance",
    "high brushes", "dualopening WeChat", "call quality", "Video", "felt", "Before the launch", "configurations are not castrated", "many aspects", "updating", "50x zoom", "daily schedule of", "processor",
    "high end", "overall strength", "commonly used function keys", "Weibo", "highbrush", "update frequency", "team battle", "maintenance", "no 2K", "lag", "other places", "Battery life", "ghost shadow",
    "Basic photography", "kings", "fingerprint unlocking speed", "wideangle", "line quality", "Oled", "playing games", "marketing model", "E5 material", "heat", "symmetrical dual speakers", "slow charging",
    "signals", "change hands in the second time", "color adjustment", "direct effect", "dual telephoto", "frontfacing camera", "work configuration", "ip68", "thickness", "feeling", "photograph",
    "stacking materials", "sold", "2K screen", "volume", "external screen ratio", "charging experience", "whole back panel", "single cell", "network", "home button", "camera effect", "bangs", "digging holes",
    "charging speed", "charging cable", "MediaTek", "localization", "partition", "Exterior", "lasts", "feels", "fingerprints on the back", "3X telephoto", "apperance value", "Snapdragon 625",
    "oneui function", "earphones with dual speakers", "Waterproof", "40W fast charging", "taking photos", "mobile phone", "fingerprints", "generally", "high refresh rate experience", "shooting experience",
    "camera hardware", "Running points", "GN2", "micro gimbal", "wireless", "camera photos", "Smooth", "rightangle side", "camera gameplay", "angle of the screen", "high", "ceramic body", "use", "computer",
    "Play the Honor of Kings", "kill the background", "hand", "telephoto solution", "imaging quality", "Texture", "product control", "long focus", "network signal", "system mechanism", "screen brightness",
    "designed", "linear motors", "refresh", "run the memory", "5G", "system operation", "Zaxis motor", "smallscreen", "color difference", "system translation", "OLED screen", "aftersale", "apps", "periphery",
    "heat dissipation stack", "color", "not a 100W", "686", "ack cover", "overall performance", "Three cameras", "2k straight screen", "grip feeling", "system recovery", "cmos", "shooting", "game mode",
    "killing the background situation", "practical", "cpu physique", "stock", "killing the background", "hard screen", "x motor", "front fingerprint", "algorithm photography", "14", "batteery life",
    "product", "rotor motor", "too poor", "overall", "touch screen experience", "memory", "dual speakers", "WiFi", "look", "video recording experience", "first generation UI", "performance scheduling",
    "configuration", "periscope lens", "level", "photo and video experience", "taking pictures", "spare", "flexible screen", "charging logic", "rendering", "Feeling", "Algorith", "secondary screen",
    "personalization, life and intelligence", "high light suppression", "interaction", "selling points", "4000 battery", "gap in animation", "permeability", "unlocking speed", "hollow in the middle",
    "reduce", "camera capability", "highdefinition screen", "system", "oil layer", "charges", "8128", "playing game", "quasi", "experience of", "hardware configuration", "textured", "typing response",
    "holding feel", "offline ability", "835", "15.1 system", "sense of power consumption", "electricity", "view", "curved screen", "smart refresh rate", "overall use", "frame feel", "imx766v",
    "four curved surfaces", "original price", "industrial design", "sensor antishake", "functional", "2x", "overall configuration", "medium and low load", "ui", "outer screen", "dropdown search", "software",
    "Shooting", "fullfocus zoom", "looking obliquely", "calling for a voice call", "AI algorithm", "background cut", "JN1 super wideangle", "use Taobao", "main configuration", "play the king",
    "desktop setting", "wireless charger", "dualopening work", "initial pricing", "video experience", "Selfie", "color reproduction", "took pictures", "kills the background", "Camera", "video quality",
    "good camera", "last", "storage", "fluency", "system response", "function", "pair of digging holes", "reputation", "A15", "bright middle frame", "PPI", "take good photos", "1080P", "system functionality",
    "telephoto photography", "photography", "emergency backup", "other aspects", "marketing", "suspension and antishake", "indoor", "king", "cost performance ratio", "Hongmeng system", "65W", "colors",
    "signal", "optical image stabilization", "hot", "Charging", "threecamera color", "ultrawide", "backstage", "powerefficient", "borders", "zaxis motor", "The feel", "periscope telephoto", "space",
    "diamondlike arrangement", "heat control", "teamfights", "looks", "experiencing", "voltage", "playing the game", "infrared", "100w", "straight screen", "static imaging", "white balance of a few cameras",
    "panel", "everything", "systems", "ten times the telephoto", "dualspeaker", "sound quality", "battery", "dual support", "standby power", "repair rate", "color cast", "volume button",
    "high frequency pwn dimming", "so many interesting icons", "telephoto camera", "palying games", "2k small screen", "sense of excessive control of the sensor", "film", "Xaxis linear motor",
    "bright silver", "system update", "flexible", "kill background program", "Kirin 990", "transparent shells", "brand", "singlespeaker and zaxis motor", "screenshot", "R angle", "Front camera",
    "multi screen", "firmware", "sales", "Comprehensive", "lens arrangement", "shoot video", "looking", "Taking pictures during the day", "120W", "take a photo", "audio", "big", "overall quality", 
    "ceramic back cover", "scheduled", "full lens night view mode", "video ability", "Dimensity 700", "gaming", "after sales policy", "network will be disconnected", "real full screen", 
    "negative optimization", "generate heat", "logo", "glass back cover", "ColorOS", "hold", "shortcomings", "beauty algorithm", "antishake", "120W fast charge", "performance release", "search on the side",
    "Taking photo", "amount of light", "telephoto macro", "mobile games", "use feel", "System", "appearance value", "Face unlock", "energy consumption", "folding screen", "zoom", "wideangle and telephoto",
    "Screen", "full screen", "curve", "after sales", "main, wide and long", "use cycle", "big battery", "8gen1", "Snapdragon 855", "highlights", "check my Moments", "video", "four speakers",
    "appearance, technology", "reliability of taking pictures", "standby", "speed", "AI recognition", "Samsung screens", "play Honor of Kings", "border", "fever", "longrange", "wear level", "videography",
    "screen look and feel", "screen quality", "other hardware", "interface", "side margins of the game", "color sharpening", "WIFI", "Playing Chicken", "sales strategy", "products", "upgrades", 
    "Playing the game", "super night scene video", "diving", "freezing", "way it is arranged", "all aspects", "response speed", "Xiaolong", "wideangle lens", "outdoors", "color scheme", "touch", "control", 
    "photo shoot", "Monster mode", "camera module", "hardware", "ghosting", "loss", "running speed", "battery capacity", "creases of the folding screen", "refresh rate of 120", "resolution", "no 2k", 
    "Quality control", "silicone case", "fake background", "short boards", "photos", "news vibration", "sound", "baseband power consumption", "power drop", "pictures", "main camera image", 
    "cost effectiveness", "Portrait lens", "design", "body design", "fivefold potential telephoto", "play", "night mode is forced", "curvature", "sensor", "dropped frames", "aperture", "video recording", 
    "components", "update", "camera modules", "ppi", "symmetrical Harmancat", "Memory", "focusing", "Gesture operation", "dropped", "defective rate", "area of the hot plate", "back design", 
    "rendering picture", "battery power", "1080PLCD", "charger", "phone separation", "front view", "heating", "charge faster", "lose power", "dual main camera", "screen camera", "dark light", "algorith", "black edge of the chin", "software system", "curved surface", "WeChat", "brightness", "cool guy pink", "image systems", "debugging", "smoothness", "Taking portrait photos", "chips", "photo effect", "images", "Localized", "Y axis", "WiFi disappeared and WiFi", "stores cut", "continuity of animation", "color of photos", "Running", "data migration", "navigate", "standby time and battery life", "starting price", "aftersales service", "4500mah battery", "drop power", "creativity", "volume keys", "hand feeling", "shooting ppt", "take pictures", "ultrawideangle", "ios", "System fluency", "HDR", "speaker", "linear motor is available in the Mi 2", "super smooth", "outsole super wideangle", "costeffective", "filming rate", "Power consumption", "consumers experience", "gap", "1080 processor", "native system", "basically not hot", "recognizable", "stocking situation", "high brush", "sell", "iOS", "white balance", "video capabilities", "cooling system", "shoot", "overheating", "color of the back", "page", "life", "flash", "take photos casually", "9000", "overheat", "Ye Xiao", "system optimization", "intelligence of the input method", "small screen", "photography experience", "take pictures casually", "performance", "taste", "functions", "front camera", "powered down", "APP", "5x optical change", "four a76 cores", "photography camera module", "970", "underscreen fingerprint", "screen, camera", "Other experience", "dual batteries", "camera experience", "Photography", "4500 battery", "system upgrades and maintenance", "pixels", "image configuration", "small windows", "cos12", "stuttering, heat",
    "dualcard experience", "waterfall screen", "120W charging", "silver", "night scene", "hand feels", "wired", "software to be coldstarted", "highfrequency PWM", "videos", "selfie effect", "UI", "human voice mode", "Playing games", "watching the video",
    "100 million", "bottom", "CPU", "watching parameters", "front fingerprint recognition", "Other aspects", "everything else", "fuselage", "surf the Internet", "Background bottom layer", "others",
    "speed of response", "Charge", "Z axis motor", "speed of his price", "gaming experience", "filming speed", "small window mode", "wireless charging", "play Kings Glory", "C11", "heat generation and power",
    "ease of use", "long screen", "human voice", "smooth", "selfies", "frame rate", "lcd", "sensors", "game", "listening to songs", "depress highlights", "adjustment", "photo experience", "rest", "back",
    "adaptation", "drop feels", "portrait lens", "shooting video", "effect of taking pictures", "external playback", "speed of taking pictures", "heat radiation", "845", "aftersales", "Samsung screen", "system fluency", "aftersales maintenance stores", "faster charge", "endurance", 
    "under the screen", "Feels", "animation", "vibration", "grip", "diving space", "high frame rate of King of", "game experienc", "filming time", "hole", "camera imaging", "dualcell", "color accuracy", "66w fast charge", "888", "1080P Samsung screen", "system stability", "tuning of taking pictures", "Aesthetics", "propaganda", "middle frame", "spare machine", "bright", "IP68", "castration", "work software", "highend machine sales",
    "1080", "selfie", "design idea", "actual shooting", "imx582", "chin", "Signal", "Dimensity 800", "hand feel", "originally beautify", "flickering", "screen", "internal screen", "a15", "turn on the camera", "other configurations", "front and back of", "camera function", "main camera of the camera", "algorithm", "screens", 
    "battery life of", "rear module", "fast charge", "Overheat", "night scene of the camera", "Notification push", "soc", "original fast charge", "upper limit", "digitalization of film M", "keep the screen on", "actual experience", "transparency", "LCD screens", "extreme mode", "fast charging", "color authenticity", "Taking photos", "post camera", "highbrush experience", "optimization strength", "Telephoto", "craftsmanship", "value", "price", "night glare suppression", "chip", "color matching", "record a video", "operational experiences",
    "slide", "discount", "viewing angle", "consumes", "used", "quality control", "consumption", "optimized", "4curved surface", "Leica", "bare machine feels", "priceperformance", "5 telephoto", "color during the day", "Screen arrangement", "Others", "signal experience", "fringe screen", "experience", "cad", "global DC", "package", "fever and run slow",
    "lcd screen", "identifiable", "night view", "33w", "lenses", "front", "waterproof", "software ecosystems", "face value", "true full screen", "game performance", "starting camera", "material", 
    "Samsung flexible screen", "photography algorithms", "adjusted", "strobe difference", "display effect", "size", "focus", "handling", "look and feel", "touch rate", "replace the battery", "Overall", 
    "some aspect", "ultrasonic microcloud platform", "unlock", "Zeiss", "typing", "actual performance", "night shots", "balanced mode", "running memory", "custom cmos tuning", "charging", "Small settings",
    "small problems", "vlog shooting", "takes pictures", "periscope", "mobile phone size", "telephoto lens", "short focus", "daily", "high frequency pwm", "lens module", "dimming", "advertisements",
    "5G signal", "overclocked", "refresh rate", "control experience", "small faults", "core of 990", "Huaxing Optoelectronics screen", "notification bar information", "viewfinder frame", "temperament", 
    "workmanship", "2K LCD", "speakers", "quality", "goodlooking", "light blue", "threedimensional", "photography of people", "top screen", "photo quality", "switching cameras", "quality of the film", 
    "system album", "ultrasonic fingerprint", "Samsungs 2k screen", "Single speaker, plastic body", "high refresh rate", "portability", "diamond", "down", "small window experience", "battery loss", 
    "waterproof and dustproof", "65w", "imaging effect", "folding technique", "power consumption optimization", "metal body", "speed of opening", "shape", "high frame rate", "optimization of software", 
    "coloros", "heat dissipation", "120W fast charging", "rear camera", "better", "loudspeaker", "image system", "power consumption", "picture", "shipments", "forehead", "battery life", 
    "software color matching", "clarity", "8882k4000", "fingerprint", "foundation", "appearance design", "openings", "photo selection rate", "WPS", "fast", "sync across devices", "after the launch",
    "ecological", "adaptive refresh", "image", "motor", "mode", "flash memory", "film effect", "display frame rate scheduling", "color contrast", "cameras", "Hongmeng", "direct screens", "67w fast charge",
    "singlecore performance of the large core", "record video", "computing power", "Battery", "wifi", "quality of the main camera", "portrait", "freeze", "night scenes", "shoot videos", 
    "overall or SOOC quality", "MIUI", "quality of the pictures", "standby mode", "welding process", "black border", "swipe on Weibo", "call recording", "LCD screen", "play the glory of the king", "ISP", "specifications"]
if Path("force_tokens.json").is_file():
    with open("force_tokens.json", 'r') as f:
        force_tokens = json.load(f)

cate_list = {
    "rest14": rest_aspect_cate_list,
    "rest15": rest_aspect_cate_list,
    "rest": rest_aspect_cate_list,
    "rest16": rest_aspect_cate_list,
    "laptop": laptop_aspect_cate_list,
    "laptop14": laptop_aspect_cate_list,
    "phone": phone_aspect_cate_list
}

task_data_list = {
    "aste": ["laptop14", "rest14", "rest15", "rest16"],
    "tasd": ['rest15', "rest16"],
    "acos": ['laptop16', "rest16"],
    "asqp": ['rest15', "rest16"],
    "diaasq": ["phone"],
}
force_words = {
    'aste': {
        'rest15': list(senttag2opinion.values()) + ['[SSEP]'],
        'rest16': list(senttag2opinion.values()) + ['[SSEP]'],
        'rest14': list(senttag2opinion.values()) + ['[SSEP]'],
        'laptop14': list(senttag2opinion.values()) + ['[SSEP]']
    },
    'tasd': {
        "rest15": rest_aspect_cate_list + list(sentword2opinion.values()) + ['[SSEP]'],
        "rest16": rest_aspect_cate_list + list(sentword2opinion.values()) + ['[SSEP]']
    },
    'acos': {
        "rest": rest_aspect_cate_list + list(sentword2opinion.values()) + ['[SSEP]'],
        "laptop": laptop_aspect_cate_list + list(sentword2opinion.values()) + ['[SSEP]'],
    },
    'asqp': {
        "rest15": rest_aspect_cate_list + list(sentword2opinion.values()) + ['[SSEP]'],
        "rest16": rest_aspect_cate_list + list(sentword2opinion.values()) + ['[SSEP]'],
    },
    'diaasq': {
        "phone": phone_aspect_cate_list + list(sentword2opinion.values()) + ['[SSEP]'],
    }
}


optim_orders_all = {
            "aste": {
                "laptop14": [
                    '[O] [A] [S]', '[A] [O] [S]', '[O] [S] [A]',
                    '[A] [S] [O]', '[S] [O] [A]', '[S] [A] [O]'
                ],
                "rest14": [
                    '[O] [A] [S]', '[O] [S] [A]', '[A] [O] [S]',
                    '[A] [S] [O]', '[S] [O] [A]', '[S] [A] [O]'
                ],
                "rest15": [
                    '[A] [O] [S]', '[O] [A] [S]', '[O] [S] [A]',
                    '[A] [S] [O]', '[S] [O] [A]', '[S] [A] [O]'
                ],
                "rest16": [
                    '[O] [A] [S]', '[A] [O] [S]', '[O] [S] [A]',
                    '[A] [S] [O]', '[S] [O] [A]', '[S] [A] [O]'
                ],
            },
            "tasd": {
                "rest15": [
                    '[A] [C] [S]', '[A] [S] [C]', '[C] [S] [A]',
                    '[C] [A] [S]', '[S] [C] [A]', '[S] [A] [C]'
                ],
                "rest16": [
                    '[A] [C] [S]', '[A] [S] [C]', '[C] [S] [A]',
                    '[C] [A] [S]', '[S] [C] [A]', '[S] [A] [C]'
                ]
            },
            "acos": {
                "laptop16": [  # ot null -> sp
                    '[A] [O] [S] [C]', '[A] [S] [O] [C]',
                    '[A] [O] [C] [S]', '[O] [A] [S] [C]',
                    '[O] [A] [C] [S]', '[A] [S] [C] [O]',
                    '[A] [C] [O] [S]', '[O] [C] [A] [S]',
                    '[O] [S] [A] [C]', '[A] [C] [S] [O]',
                    '[O] [C] [S] [A]', '[O] [S] [C] [A]',
                    '[S] [A] [O] [C]', '[C] [O] [A] [S]',
                    '[C] [S] [A] [O]', '[C] [A] [O] [S]',
                    '[C] [S] [O] [A]', '[C] [O] [S] [A]',
                    '[S] [O] [A] [C]', '[C] [A] [S] [O]',
                    '[S] [O] [C] [A]', '[S] [C] [O] [A]',
                    '[S] [A] [C] [O]', '[S] [C] [A] [O]'
                ],
                "rest16": [  # ot null -> sp
                    '[A] [O] [S] [C]', '[A] [O] [C] [S]',
                    '[A] [S] [O] [C]', '[O] [A] [C] [S]',
                    '[O] [A] [S] [C]', '[O] [S] [C] [A]',
                    '[A] [C] [O] [S]', '[O] [C] [A] [S]',
                    '[O] [S] [A] [C]', '[A] [S] [C] [O]',
                    '[A] [C] [S] [O]', '[O] [C] [S] [A]',
                    '[C] [O] [A] [S]', '[C] [A] [O] [S]',
                    '[C] [S] [O] [A]', '[C] [O] [S] [A]',
                    '[S] [A] [O] [C]', '[C] [S] [A] [O]',
                    '[C] [A] [S] [O]', '[S] [O] [A] [C]',
                    '[S] [C] [O] [A]', '[S] [O] [C] [A]',
                    '[S] [C] [A] [O]', '[S] [A] [C] [O]'
                ],
            },
            "asqp": {
                "rest15": [
                    '[A] [O] [S] [C]', '[O] [A] [C] [S]',
                    '[A] [O] [C] [S]', '[O] [A] [S] [C]',
                    '[O] [S] [C] [A]', '[A] [S] [O] [C]',
                    '[O] [C] [A] [S]', '[O] [S] [A] [C]',
                    '[A] [C] [O] [S]', '[O] [C] [S] [A]',
                    '[A] [C] [S] [O]', '[C] [O] [A] [S]',
                    '[A] [S] [C] [O]', '[C] [A] [O] [S]',
                    '[C] [S] [O] [A]', '[C] [O] [S] [A]',
                    '[C] [S] [A] [O]', '[C] [A] [S] [O]',
                    '[S] [A] [O] [C]', '[S] [O] [A] [C]',
                    '[S] [C] [O] [A]', '[S] [O] [C] [A]',
                    '[S] [C] [A] [O]', '[S] [A] [C] [O]'
                ],
                "rest16": [
                    '[O] [A] [C] [S]', '[A] [O] [S] [C]',
                    '[O] [A] [S] [C]', '[O] [S] [C] [A]',
                    '[A] [O] [C] [S]', '[O] [S] [A] [C]',
                    '[O] [C] [A] [S]', '[A] [S] [O] [C]',
                    '[O] [C] [S] [A]', '[A] [C] [O] [S]',
                    '[A] [C] [S] [O]', '[C] [O] [A] [S]',
                    '[A] [S] [C] [O]', '[C] [A] [O] [S]',
                    '[C] [O] [S] [A]', '[C] [S] [O] [A]',
                    '[C] [S] [A] [O]', '[S] [A] [O] [C]',
                    '[C] [A] [S] [O]', '[S] [O] [A] [C]',
                    '[S] [O] [C] [A]', '[S] [C] [O] [A]',
                    '[S] [C] [A] [O]', '[S] [A] [C] [O]'
                ],
            },
            "diaasq": {
                "phone": [
                    '[A] [O] [S] [C]', '[O] [A] [C] [S]',
                    '[A] [O] [C] [S]', '[O] [A] [S] [C]',
                    '[O] [S] [C] [A]', '[A] [S] [O] [C]',
                    '[O] [C] [A] [S]', '[O] [S] [A] [C]',
                    '[A] [C] [O] [S]', '[O] [C] [S] [A]',
                    '[A] [C] [S] [O]', '[C] [O] [A] [S]',
                    '[A] [S] [C] [O]', '[C] [A] [O] [S]',
                    '[C] [S] [O] [A]', '[C] [O] [S] [A]',
                    '[C] [S] [A] [O]', '[C] [A] [S] [O]',
                    '[S] [A] [O] [C]', '[S] [O] [A] [C]',
                    '[S] [C] [O] [A]', '[S] [O] [C] [A]',
                    '[S] [C] [A] [O]', '[S] [A] [C] [O]'
                ],
            },
        }


heuristic_orders = {
    'aste': ['[A] [O] [S]'],
    'tasd': ['[A] [C] [S]'],
    'asqp': ['[A] [O] [C] [S]'],
    'acos': ['[A] [O] [C] [S]'],
    'diaasq': ['[A] [O] [S]'],
}