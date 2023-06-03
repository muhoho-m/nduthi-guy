# import pyswahili
# import python

class NduthiGuy:
    # msee wa nduthi anainiitialize na jina, with an empty list of crates and requests
    def __init__(self, jina):
        self.jina = jina
        self.crates = []
        self.requests_track = []

    def ongeza_crate(self, jina_ya_crate,
                     mkate_za_brown, mkate_za_white):
        # crate ikiwekwa kwa nduthi inapewa jina, mkate ziko za white
        # na za brown. kila crate iko na mikate 24
        # na mkate za brown lazima ziwe one third of the total for all crates
        if mkate_za_brown > 8:
            excess_za_brown = mkate_za_brown - 8
            mkate_za_brown = mkate_za_brown - excess_za_brown
            print(f"Excess ya brown imetolewa: {excess_za_brown}")
        # tukianza, crate moja ni ya kuchukua spoils kwa maduka thus enye iko na zero
        # everything naipea jina spoilt
        if mkate_za_brown < 8 and mkate_za_brown != 0:
            deficit_za_brown = 8 - mkate_za_brown
            # kama mkate za brown hazifiki nane tunaongeza
            mkate_za_brown = mkate_za_brown + deficit_za_brown
            print(f"Mkate za brown zimeongezwa ni {deficit_za_brown}")
        if mkate_za_white > 16:
            excess_za_white = mkate_za_white - 16
            # kama mkate za white ni mingi tunatoa
            mkate_za_white = mkate_za_white - excess_za_white
            print(f"Excess ya white imetolewa: {excess_za_white}")
        if mkate_za_white < 16 and mkate_za_white != 0:
            deficit_za_white = 16 - mkate_za_white
            # kama mkate za white ni kidogo tunaongeza
            mkate_za_white = mkate_za_white + deficit_za_white
            print(f"Mkate za white zimeongezwa ni {deficit_za_white}")
        if mkate_za_brown == 0 and mkate_za_white == 0:
            mkate_za_brown = 0
            mkate_za_white = 0
            # kama crate haina any, hio itakua ya kuchukua spoils
            jina_ya_crate = "Spoit crate"

        # details za crate naziweka kwa dictionary for easier access badae
        crate = {
            "jina": jina_ya_crate,
            "mkate_za_brown": mkate_za_brown,
            "mkate_za_white": mkate_za_white
        }
        self.crates.append(crate)

    def details_za_crates(self):
        # nikitaka kuona details zote ziko kwa crate nazitoa kwa dictionary
        # na kuziprint out
        print(f"kuna crates {len(self.crates)}")
        for crate in self.crates:
            jina = crate["jina"]
            mkate_za_brown = crate["mkate_za_brown"]
            mkate_za_white = crate["mkate_za_white"]
            print(f"{jina} iko na mikate za brown {mkate_za_brown} na za white {mkate_za_white}")

    def chukua_request(self, mtu_wa_duka):
        # hapa msee wa nduthi anachukua request ya mtu wa duka akitaka mikate
        mikate = mtu_wa_duka.requests
        for request in mikate:
            self.request_za_brown = request["mkate_za_brown"]
            self.request_za_white = request["mkate_za_white"]
            jina = mtu_wa_duka.name
            print(f"Mtu wa duka {jina} anataka brown {self.request_za_brown} na white {self.request_za_white}")

    def peana_mikate(self, mtu_wa_duka):
        # msee wa nduthi akichukua request anapea msee wa duka mikate anataka
        # kulingana na kimate ako nazo
        for crate in self.crates:
            jina = crate["jina"]
            mkate_za_brown = crate["mkate_za_brown"]
            mkate_za_white = crate["mkate_za_white"]

            if mkate_za_brown >= int(self.request_za_brown):
                mkate_za_brown_anapeana = int(self.request_za_brown)
                mkate_brown_zimebaki = mkate_za_brown - mkate_za_brown_anapeana
                mkate_za_brown = mkate_brown_zimebaki
                crate["mkate_za_brown"] = mkate_za_brown
                print(f"{mtu_wa_duka.name} amepewa mikate za brown {mkate_za_brown_anapeana}"
                      f" kutoka kwa {jina}")

            if mkate_za_brown < self.request_za_brown:
                excess_requests = self.request_za_brown - mkate_za_brown

            if mkate_za_white >= int(self.request_za_white):
                mkate_za_white_anapeana = int(self.request_za_white)
                mkate_white_zimebaki = mkate_za_white - mkate_za_white_anapeana
                mkate_za_white = mkate_white_zimebaki
                crate["mkate_za_white"] = mkate_za_white
                print(f"{mtu_wa_duka.name} amepewa mikate za white {mkate_za_white_anapeana}"
                      f" kutoka kwa {jina}")


class Mtu_Wa_Duka:
    # mtu wa duka anainnitialize na jina na list empty ya requests
    # hii list ndo msee wa nduthi atatumia kumpatia mikate
    def __init__(self, name):
        self.name = name
        self. requests = []

    def tuma_request(self):
        print("Unataka brown ngapi >> ")
        mkate_za_brown = input()
        print("Unataka white ngapi >> ")
        mkate_za_white = input()
        request = {"mkate_za_brown": mkate_za_brown,
                   "mkate_za_white": mkate_za_white}
        self.requests.append(request)
