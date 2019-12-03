"""Leetcode 706. Design HashMap
Easy

URL: https://leetcode.com/problems/design-hashmap/

Design a HashMap without using any built-in hash table libraries.

To be specific, your design should include these functions:

- put(key, value) : Insert a (key, value) pair into the HashMap. 
  If the value already exists in the HashMap, update the value.
- get(key): Returns the value to which the specified key is mapped, 
  or -1 if this map contains no mapping for the key.
- remove(key) : Remove the mapping for the value key 
  if this map contains the mapping for the key.

Example:
MyHashMap hashMap = new MyHashMap();
hashMap.put(1, 1);
hashMap.put(2, 2);
hashMap.get(1);            // returns 1
hashMap.get(3);            // returns -1 (not found)
hashMap.put(2, 1);         // update the existing value
hashMap.get(2);            // returns 1
hashMap.remove(2);         // remove the mapping for 2
hashMap.get(2);            // returns -1 (not found)

Note:
- All keys and values will be in the range of [0, 1000000].
- The number of operations will be in the range of [1, 10000].
- Please do not use the built-in HashMap library.
"""

class MyHashMap(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.capacity = 8
        self.size = 0
        self.map = [[None, None]] * 8
        self.load_factor = 2.0 / 3

    def _hash(self, key):
        return key % self.capacity

    def _rehash(self, hash_key):
        return (5 * hash_key + 1) % self.capacity

    def put(self, key, value):
        """
        Value will always be non-negative.

        :type key: int
        :type value: int
        :rtype: None
        """
        # If hashmap size is larger than capacity, double it and copy keys & values.
        if float(self.size) / self.capacity >= self.load_factor:
            self.capacity <<= 1
            new_map = [[None, None]] * self.capacity

            for i in range(self.capacity >> 1):
                if self.map[i][0] >= 0:
                    h = self._hash(self.map[i][0])

                    while new_map[h][0] is not None:
                        h = self._rehash(h)

                    new_map[h] = self.map[i]

            self.map = new_map

        # Get hashed key and apply Open Addressing for collision.
        h = self._hash(key)

        while self.map[h][0] is not None:
            if self.map[h][0] == key:
                self.map[h][1] = value
                return None
            else:
                h = self._rehash(h)
                if self.map[h][0] == -1:
                    break

        self.map[h] = [key, value]
        self.size += 1
        # print self.map

    def get(self, key):
        """
        Returns the value to which the specified key is mapped, 
        or -1 if this map contains no mapping for the key.

        :type key: int
        :rtype: int
        """
        h = self._hash(key)

        while self.map[h][0] is not None:
            if self.map[h][0] == key:
                return self.map[h][1]
            else:
                h = self._rehash(h)

        return -1

    def remove(self, key):
        """
        Removes the mapping of the specified value key 
        if this map contains a mapping for the key.
        
        :type key: int
        :rtype: None
        """
        h = self._hash(key)

        while self.map[h][0]:
            if self.map[h][0] == key:
                self.map[h] = [-1, None]
                self.size -= 1
                return None
            else:
                h = self._rehash(h)


def main():
    # hashMap = MyHashMap()
    # hashMap.put(1, 1)
    # hashMap.put(2, 2)
    # print hashMap.get(1)             # returns 1
    # print hashMap.get(3)             # returns -1 (not found)
    # hashMap.put(2, 1)                # update the existing value
    # print hashMap.get(2)             # returns 1
    # hashMap.remove(2)                # remove the mapping for 2
    # print hashMap.get(2)             # returns -1 (not found)

    methods = ["MyHashMap","get","get","put","put","get","get","put","put","get","put","put","put","put","put","get","get","put","put","put","get","put","put","put","put","put","get","put","put","remove","put","put","put","put","get","put","put","remove","put","put","put","remove","remove","remove","get","put","get","remove","put","put","put","put","remove","put","get","put","put","remove","put","put","put","put","put","put","remove","get","get","put","put","put","get","put","put","put","put","put","get","remove","put","remove","remove","put","put","put","put","put","put","put","put","put","put","put","put","put","put","put","get","remove","get","put","put","get","remove","remove","put","put","put","put","get","remove","put","put","put","get","put","put","put","put","remove","put","put","put","put","put","put","put","put","put","put","put","remove","put","put","get","put","put","put","put","put","put","put","remove","put","remove","put","put","put","get","put","put","get","put","get","remove","put","remove","remove","put","get","put","put","put","put","get","put","get","put","put","put","put","put","put","put","put","put","remove","put","remove","put","remove","put","put","put","put","put","put","put","put","put","put","put","get","put","put","remove","remove","put","put","put","put","get","remove","put","get","put","put","put","remove","put","put","remove","put","put","put","get","put","put","get","remove","get","put","put","put","put","put","put","put","put","remove","put","put","put","put","get","remove","put","remove","put","put","get","put","put","put","put","put","put","remove","put","put","put","remove","remove","put","put","put","remove","remove","remove","put","put","put","get","put","put","put","put","put","put","put","put","get","put","put","get","put","put","put","get","put","put","put","remove","get","get","put","put","put","put","get","put","put","put","get","put","get","put","put","put","put","put","put","put","put","put","put","get","put","put","put","put","put","put","put","put","put","put","put","put","get","get","put","put","put","put","get","put","put","put","put","put","put","put","put","get","remove","get","put","put","put","put","put","remove","remove","remove","remove","put","put","put","put","get","get","put","put","remove","put","put","put","put","put","put","put","get","put","put","put","remove","put","put","put","put","put","put","get","put","put","put","put","put","put","get","put","put","put","remove","remove","put","get","put","put","put","get","put","put","put","remove","get","remove","put","put","put","remove","get","put","put","put","put","put","put","get","put","remove","put","put","put","put","put","put","put","put","get","put","get","remove","put","put","get","put","get","remove","put","get","remove","put","get","get","put","get","remove","put","remove","remove","put","remove","put","put","put","remove","put","put","put","get","put","put","get","put","remove","put","put","put","get","put","get","put","get","remove","remove","put","put","put","get","put","get","remove","put","put","put","put","put","put","put","put","get","put","put","put","put","get","put","put","put","put","get","put","put","put","put","put","put","put","put","get","get","put","remove","put","remove","put","put","remove","put","remove","get","put","put","put","get","put","put","put","get","get","remove","remove","put","put","put","put","put","put","put","put","put","remove","get","remove","get","put","get","remove","put","put","put","put","put","get","remove","put","put","put","remove","put","put","put","put","put","get","put","get","put","put","put","put","put","put","put","put","put","put","get","put","put","remove","get","get","put","get","put","get","put","put","remove","remove","put","put","put","put","put","get","get","get","remove","get","put","put","remove","remove","put","remove","put","get","get","put","put","put","put","put","get","remove","put","put","remove","remove","put","put","remove","put","get","get","remove","put","put","put","put","put","remove","put","put","put","put","put","put","put","put","put","put","remove","put","put","get","put","put","put","remove","put","put","put","put","put","put","get","remove","put","remove","put","remove","put","put","put","put","get","get","get","put","put","put","put","remove","put","get","put","put","put","put","remove","put","get","put","put","put","get","put","put","put","get","remove","remove","put","put","get","put","put","put","put","remove","put","remove","put","put","put","put","put","put","get","remove","remove","put","get","put","put","get","remove","put","get","get","get","put","remove","put","put","put","put","put","put","put","remove","put","put","put","put","put","get","put","put","put","get","put","get","put","put","get","remove","put","put","put","put","get","put","get","remove","put","put","put","remove","put","remove","get","put","put","put","put","get","put","get","put","remove","get","put","put","remove","put","put","get","put","put","put","put","remove","put","put","remove","put","put","put","get","put","put","remove","put","put","remove","get","remove","put","put","put","get","get","put","put","remove","put","put","put","put","put","put","put","put","get","remove","put","get","put","put","get","put","get","put","put","get","put","put","put","remove","put","remove","put","put","put","put","put","put","put","put","put","put","get","put","remove","remove","put","get","put","put","put","put","remove","get","put","get","put","put","put","get","put","put","put","put","get","remove","put","put","get","remove","put","put","put","get","put","put","put","put","get","put","put","remove","remove","put","get","get","put","put","put","put","put","put","put","put","get","put","put","put","put","put","put","put","remove","put","put","put","put","put","put","put","get","put","put","put","put","remove","put","remove","put","put","get","put","put","put","put","put","put","put","remove","remove","remove","put","put","put","put","put","remove","put","put","put","put","put","put","put","put","put","put","get","put","put","put","put","put","remove","put","get","put","put","remove","get","put","remove","remove","get","put","put","remove","put","get","get","put","put","put","put","get","remove","put","remove","put","put","put","put","get","remove","put","put","put","put","put","get","put","put","put","put","put","put","remove","remove","put","put","put","put","remove","remove","put","put","put"]
    args = [[],[222],[779],[565,194],[4,73],[565],[4],[494,654],[864,696],[494],[332,682],[96,829],[313,878],[140,924],[406,160],[602],[494],[886,303],[249,695],[791,609],[399],[102,984],[705,165],[883,842],[341,790],[182,558],[157],[55,927],[626,209],[96],[733,949],[241,482],[40,360],[247,20],[152],[596,170],[926,111],[276],[822,579],[622,22],[783,943],[175],[822],[749],[249],[656,544],[626],[626],[997,349],[129,347],[254,226],[835,383],[247],[789,898],[149],[770,992],[321,395],[789],[367,872],[454,685],[305,933],[79,779],[975,915],[301,4],[546],[783],[321],[503,1],[3,463],[96,422],[293],[819,782],[676,575],[867,763],[630,965],[566,632],[523],[680],[460,284],[254],[596],[896,67],[571,689],[113,637],[943,247],[283,281],[595,875],[268,692],[421,713],[489,546],[917,731],[21,719],[969,977],[521,176],[831,113],[700,151],[971],[378],[573],[208,368],[261,922],[515],[3],[638],[281,841],[819,238],[904,399],[254,598],[997],[406],[294,795],[834,170],[410,941],[972],[696,229],[792,161],[495,918],[320,4],[410],[471,508],[698,596],[949,66],[703,95],[608,801],[609,634],[64,276],[882,637],[326,536],[103,71],[977,758],[612],[194,250],[643,813],[601],[609,229],[350,623],[463,654],[954,215],[852,741],[145,345],[230,985],[181],[330,931],[277],[747,220],[256,443],[217,92],[984],[256,784],[689,703],[161],[161,764],[573],[371],[41,509],[190],[278],[525,997],[325],[880,812],[352,630],[999,733],[660,552],[657],[216,686],[352],[352,90],[456,92],[339,480],[520,849],[664,984],[804,906],[375,570],[685,618],[51,968],[364],[260,47],[79],[943,139],[247],[321,725],[392,505],[121,395],[852,305],[131,671],[486,689],[528,51],[736,708],[894,479],[361,222],[414,316],[256],[181,299],[358,838],[186],[320],[22,109],[311,60],[825,853],[10,745],[358],[567],[96,295],[660],[138,621],[631,112],[918,859],[622],[670,402],[143,944],[313],[832,395],[311,408],[143,158],[410],[987,361],[649,100],[235],[880],[832],[52,541],[308,99],[716,308],[484,502],[437,236],[765,889],[125,643],[339,43],[895],[600,225],[134,878],[11,482],[96,133],[11],[96],[721,215],[350],[252,225],[30,316],[770],[625,246],[437,832],[213,674],[174,562],[662,876],[188,195],[308],[389,709],[126,190],[249,919],[791],[241],[333,747],[742,919],[460,16],[786],[92],[794],[108,215],[319,801],[963,737],[700],[86,804],[552,822],[228,476],[814,593],[558,786],[174,848],[846,656],[386,945],[80],[293,923],[838,604],[595],[737,250],[883,663],[247,834],[263],[739,714],[521,784],[196,294],[513],[352],[596],[245,761],[732,395],[232,117],[543,539],[751],[29,372],[375,680],[688,544],[261],[480,826],[243],[461,661],[725,115],[137,303],[590,90],[111,325],[744,852],[460,944],[909,811],[420,621],[476,987],[803],[493,689],[576,271],[93,592],[566,796],[478,139],[376,757],[5,466],[446,440],[152,465],[389,111],[134,258],[399,350],[476],[700],[906,214],[701,239],[578,124],[33,711],[638],[358,301],[332,969],[747,614],[466,900],[714,21],[272,697],[22,526],[713,147],[93],[649],[249],[497,187],[282,99],[89,416],[374,160],[952,107],[253],[319],[444],[4],[94,315],[692,278],[395,923],[403,91],[804],[385],[662,837],[982,48],[725],[303,146],[585,894],[295,830],[583,153],[643,621],[902,408],[92,455],[561],[648,941],[525,960],[340,477],[108],[55,988],[730,852],[483,196],[438,289],[325,277],[394,59],[29],[112,401],[247,192],[821,111],[110,127],[546,653],[559,826],[471],[546,865],[468,167],[437,877],[94],[688],[648,496],[982],[414,858],[167,815],[673,841],[905],[35,998],[268,684],[365,457],[74],[92],[942],[470,922],[716,876],[461,326],[131],[254],[228,801],[148,882],[438,761],[35,328],[522,453],[411,187],[578],[574,126],[395],[957,688],[843,180],[380,563],[470,182],[734,781],[579,318],[608,180],[194,730],[478],[963,854],[365],[819],[544,700],[218,521],[951],[113,611],[311],[676],[920,299],[350],[926],[285,65],[639],[454],[693,557],[384],[287],[469,637],[301],[486],[945,271],[145],[225,579],[477,276],[288,428],[24],[521,782],[479,523],[673,539],[349],[611,870],[578,693],[909],[125,818],[630],[454,840],[334,205],[969,967],[143],[465,580],[332],[850,138],[140],[282],[350],[657,140],[454,379],[295,967],[260],[775,108],[742],[114],[724,440],[428,429],[759,817],[396,853],[895,888],[855,359],[523,359],[377,139],[251],[393,1],[792,930],[313,37],[755,257],[188],[330,206],[394,996],[13,93],[513,998],[390],[991,86],[119,635],[145,10],[566,96],[796,203],[473,641],[179,330],[339,174],[83],[982],[585,374],[394],[670,888],[513],[961,597],[0,246],[912],[392,887],[465],[411],[433,604],[880,760],[519,356],[724],[151,605],[247,718],[546,902],[134],[237],[839],[179],[508,804],[356,338],[480,65],[296,771],[146,663],[130,734],[894,101],[962,198],[656,678],[232],[757],[759],[763],[594,136],[793],[466],[49,745],[968,154],[620,851],[336,397],[268,646],[343],[609],[572,123],[307,246],[287,959],[578],[443,272],[912,406],[244,671],[117,202],[483,799],[218],[913,833],[145],[712,134],[862,679],[644,675],[691,672],[280,710],[577,580],[289,586],[254,322],[739,43],[450,986],[64],[585,485],[343,30],[808],[834],[485],[79,778],[949],[597,885],[211],[787,110],[363,953],[515],[107],[849,906],[534,126],[201,988],[527,467],[422,421],[909],[386],[852],[572],[13],[559,692],[303,481],[16],[693],[29,727],[334],[139,389],[568],[228],[23,525],[608,443],[190,89],[147,206],[886,905],[656],[493],[554,853],[378,373],[787],[630],[535,116],[394,564],[262],[470,147],[194],[359],[493],[325,956],[57,598],[803,316],[948,30],[149,405],[57],[846,348],[768,717],[424,332],[992,468],[310,312],[481,872],[746,728],[513,728],[247,154],[581,331],[816],[767,5],[217,128],[736],[206,472],[181,772],[186,958],[470],[919,894],[418,57],[822,71],[652,379],[465,487],[26,513],[776],[449],[364,305],[125],[125,703],[324],[40,825],[340,349],[472,994],[809,144],[532],[410],[186],[471,28],[955,661],[464,16],[529,917],[157],[532,749],[476],[323,894],[688,907],[220,603],[315,8],[380],[251,623],[590],[485,689],[429,660],[727,215],[605],[220,668],[950,337],[188,733],[308],[672],[373],[825,173],[718,93],[991],[319,557],[74,955],[10,123],[336,557],[194],[668,386],[721],[224,480],[957,268],[25,145],[259,270],[151,504],[192,68],[110],[495],[511],[944,870],[303],[877,822],[924,382],[755],[4],[78,901],[192],[770],[410],[885,40],[637],[75,416],[192,174],[0,682],[865,620],[819,12],[53,453],[667,358],[794],[956,947],[339,714],[456,168],[520,670],[285,984],[181],[20,591],[965,788],[170,379],[471],[145,842],[730],[868,675],[594,715],[933],[819],[84,163],[585,31],[127,261],[977,193],[56],[651,937],[293],[715],[636,935],[559,117],[764,970],[812],[321,322],[885],[640],[64,786],[979,439],[912,829],[404,107],[869],[909,803],[465],[98,756],[776],[138],[505,42],[890,30],[744],[36,569],[983,195],[510],[803,836],[962,33],[410,773],[72,629],[377],[259,554],[595,441],[137],[529,465],[936,434],[941,322],[160],[431,43],[597,777],[868],[889,995],[444,190],[521],[926],[208],[20,800],[547,0],[636,354],[152],[868],[421,507],[624,332],[849],[32,776],[205,387],[773,407],[805,190],[303,72],[101,607],[91,524],[922,976],[475],[717],[227,340],[120],[935,5],[371,471],[652],[287,831],[804],[727,889],[553,413],[864],[760,341],[872,779],[625,958],[682],[158,208],[171],[482,642],[317,37],[190,80],[22,773],[730,660],[37,886],[54,214],[943,558],[115,358],[172,136],[666],[948,35],[949],[421],[46,248],[713],[17,749],[979,731],[375,163],[474,14],[40],[357],[915,354],[57],[754,756],[389,832],[421,907],[869],[945,164],[676,857],[347,70],[58,936],[945],[760],[29,266],[18,856],[644],[961],[715,438],[871,637],[153,410],[58],[431,950],[156,187],[958,261],[103,455],[393],[4,211],[226,443],[302],[192],[32,455],[140],[103],[110,445],[368,564],[783,542],[185,85],[356,840],[156,169],[591,458],[923,853],[287],[543,933],[708,772],[583,338],[22,803],[92,105],[941,638],[16,922],[992],[410,415],[598,861],[311,692],[938,620],[511,466],[344,978],[223,139],[474],[681,104],[678,18],[254,575],[657,464],[838],[109,393],[484],[51,789],[570,529],[931],[886,645],[374,69],[963,962],[622,574],[434,370],[600,172],[406,336],[909],[165],[991],[871,927],[335,966],[668,687],[662,38],[397,495],[801],[146,697],[835,905],[582,24],[541,936],[59,581],[38,835],[393,220],[168,523],[276,633],[125,571],[724],[833,217],[756,816],[457,168],[508,73],[67,359],[768],[876,981],[987],[639,909],[444,815],[909],[880],[492,745],[8],[924],[25],[750,497],[987,453],[736],[208,127],[252],[86],[355,124],[33,147],[201,84],[712,165],[0],[639],[767,717],[529],[707,176],[265,281],[776,318],[834,532],[50],[838],[182,212],[950,7],[246,621],[238,348],[247,760],[282],[466,775],[45,92],[390,70],[504,230],[558,554],[990,157],[955],[330],[317,143],[677,67],[11,11],[897,213],[236],[929],[28,273],[74,408],[347,155]]
    expecteds = [None,-1,-1,None,None,194,73,None,None,654,None,None,None,None,None,-1,654,None,None,None,-1,None,None,None,None,None,-1,None,None,None,None,None,None,None,-1,None,None,None,None,None,None,None,None,None,695,None,209,None,None,None,None,None,None,None,-1,None,None,None,None,None,None,None,None,None,None,943,395,None,None,None,-1,None,None,None,None,None,-1,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,-1,None,-1,None,None,-1,None,None,None,None,None,None,349,None,None,None,None,-1,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,-1,None,None,None,None,None,None,None,None,None,None,None,None,None,-1,None,None,-1,None,-1,None,None,None,None,None,-1,None,None,None,None,-1,None,630,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,784,None,None,None,None,None,None,None,None,838,None,None,552,None,None,None,None,None,None,None,None,None,None,-1,None,None,-1,None,395,None,None,None,None,None,None,None,None,None,None,None,None,None,482,None,None,None,None,None,992,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,151,None,None,None,None,None,None,None,None,-1,None,None,875,None,None,None,-1,None,None,None,None,90,-1,None,None,None,None,-1,None,None,None,922,None,-1,None,None,None,None,None,None,None,None,None,None,-1,None,None,None,None,None,None,None,None,None,None,None,None,987,151,None,None,None,None,-1,None,None,None,None,None,None,None,None,592,None,919,None,None,None,None,None,None,None,None,None,None,None,None,None,906,-1,None,None,None,None,None,None,None,None,None,None,-1,None,None,None,None,None,None,None,None,None,None,372,None,None,None,None,None,None,508,None,None,None,None,None,None,48,None,None,None,-1,None,None,None,None,455,None,None,None,None,None,598,None,None,None,None,None,None,124,None,None,None,None,None,None,None,None,None,None,139,None,457,None,None,None,-1,None,408,None,None,-1,None,None,-1,685,None,-1,None,None,None,None,None,None,None,None,None,None,None,None,None,-1,None,None,811,None,None,None,None,None,158,None,969,None,924,None,None,None,None,None,47,None,919,None,None,None,None,None,None,None,None,None,-1,None,None,None,None,195,None,None,None,None,-1,None,None,None,None,None,None,None,None,-1,48,None,None,None,None,None,None,None,None,None,187,None,None,None,440,None,None,None,258,-1,None,None,None,None,None,None,None,None,None,None,None,None,-1,None,-1,None,-1,None,None,None,None,None,None,-1,None,None,None,None,None,None,None,None,None,None,521,None,10,None,None,None,None,None,None,None,None,None,None,276,None,None,None,170,-1,None,66,None,-1,None,None,None,None,None,None,None,None,None,811,945,305,None,93,None,None,None,None,None,None,None,-1,801,None,None,None,None,None,678,None,None,None,None,None,None,None,None,None,730,-1,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,708,None,None,None,None,None,None,None,None,None,None,-1,None,None,None,None,None,None,None,None,None,-1,-1,958,None,None,None,None,None,None,987,None,None,None,None,None,None,90,None,None,None,-1,None,None,None,-1,None,None,None,None,86,None,None,None,None,None,None,None,None,None,None,None,None,None,127,None,None,None,481,None,None,257,None,None,68,992,-1,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,772,None,None,None,28,None,852,None,None,-1,None,None,None,None,None,-1,None,923,None,None,None,None,None,None,None,-1,None,None,None,None,-1,None,487,None,None,621,None,None,None,None,None,-1,None,None,None,None,None,None,None,None,None,None,None,-1,None,None,None,None,None,None,-1,None,None,None,None,465,-1,None,None,None,None,None,None,None,None,None,None,None,-1,None,None,-1,None,None,379,None,906,None,None,696,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,-1,None,None,None,None,147,None,None,None,None,None,-1,None,-1,None,None,None,-1,None,None,None,None,164,None,None,None,675,None,None,None,None,936,None,None,None,None,1,None,None,None,None,None,924,455,None,None,None,None,None,None,None,None,831,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,14,None,None,None,None,None,None,None,None,None,-1,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,440,None,None,None,None,None,None,None,361,None,None,None,760,None,None,None,145,None,None,None,None,225,804,None,None,None,None,682,None,None,None,None,None,None,None,-1,None,None,None,None,None,None,-1,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None]
    
    def apply(method, arg, hashMap):
        if method == 'put':
            hashMap.put(arg[0], arg[1])
            return None
        elif method == 'remove':
            hashMap.remove(arg[0])
            return None
        elif method == 'get':
            return hashMap.get(arg[0])

    hashMap = MyHashMap()

    for i in range(1, len(methods)):
        result = apply(methods[i], args[i], hashMap)
        if methods[i] == 'get':
            print '-', i, methods[i], args[i], result, expecteds[i]
            assert result == expecteds[i]

if __name__ == '__main__':
    main()
