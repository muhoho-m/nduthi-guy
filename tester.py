from nduthi_guy import NduthiGuy, Mtu_Wa_Duka

nduthi_guy = NduthiGuy("Kinuthia")

nduthi_guy.ongeza_crate("crate1", 1, 20)
nduthi_guy.ongeza_crate("crate3", 0, 0)
print(nduthi_guy.details_za_crates())
# print(info1)

mtu_wa_duka = Mtu_Wa_Duka("Kamau")
mtu_wa_duka.tuma_request()

nduthi_guy.chukua_request(mtu_wa_duka)
nduthi_guy.peana_mikate(mtu_wa_duka)

