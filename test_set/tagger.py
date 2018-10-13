import codecs
# f = codecs.open(filename, encoding="utf-8")
f1 = open("diseases.txt", "r")
lst=[]
lines1 = f1.readlines()
for i in lines1:
    l=i.split()
    for j in range(0,len(l)):
        if j==0:
            lst.append(l[0])
f = open("test_questions7.output", "r")
g = {}
s = "SELECT"
p = "DISCARD"
lst1=["लक्षणों","लक्षण","संलक्षण","लक्षण-समष्टि","परिलक्षण","उत्पर्रेक","ऑर्गॅनिक","नियंत्रण","जैविक","रासायनिक","निवारक", "उपाय","कारण","वैज्ञानिक","नाम","संक्षिप्त","लक्षणों","आरंभ","उत्‍पन्न","उत्पन्नकारी","विमोचक","प्रतिक्रिया","सक्रिय","शूरू","कुद्रती","केमिकल","निरोध","रोकधाम","प्रतिकार","पर्तिबन्ध","अभिप्राय","जीव","पैदा","प्रेरित","उकसाता","संक्षिप्त","संक्षेप","मुख्तसर","लघु","फसल","मेजबान","बिमारी","अनार","रोग","कीट","पानी","रोक","कमी","नाइट्रोजन","बॉरॉन","मॅग्नीज़ियम","सलफर","ज़िंक","कॅल्षियम","सहलक्षण","आम","बॅक्टीरिया","टमाटर","बैंगन","अंगूर","वायरस","रोक","फफूँद","फफूंद"]
for j in lst1:
    lst.append(j)
lines = f.readlines()
for i in lines:
    l = i.split()
    for i in range(0, len(l)):
        g[l[0]] = l[3]
store = []
for i in lines:
    if i == "\n":
        store.append("\n");
    l = i.split()
    x = 0
    for i in range(0, len(l)):
        if x == 1:
            break
        c=0
        for item in lst:
            #print (l[1])
            if item==l[1]: 
                #print (item)
                c=1
                break
        if l[4] == "0":
            if c==1:
                store.append([l[1], l[5], l[3], "-"])
            else:
                store.append([l[1], l[5], l[3], "-"])
        else:   
            if c==1:
                store.append([l[1],l[5], l[3], g[l[4]]])
            else:
                store.append([l[1],l[5], l[3], g[l[4]]])
        x = 1
        # store[l[1]]=[g[l[4]],l[5]]
for i in store:
    print("  ".join(i))
    # print "\n"

    # print l[0],l[1],l[2],l[3],l[4]
    # (l)



