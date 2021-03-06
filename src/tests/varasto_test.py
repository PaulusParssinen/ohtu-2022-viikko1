import unittest
from varasto import Varasto

class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)
        
    def test_lisays_negative(self):
        saldo_og = self.varasto.saldo
        self.varasto.lisaa_varastoon(-1337)
        
        self.assertAlmostEqual(self.varasto.saldo, saldo_og)
    
    def test_add_too_much(self):
        self.varasto.lisaa_varastoon(self.varasto.paljonko_mahtuu() + 1)
        self.assertAlmostEqual(self.varasto.saldo, self.varasto.tilavuus)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_take_too_much(self):
        possible_to_take = self.varasto.saldo
        taken = self.varasto.ota_varastosta(self.varasto.saldo + 1)
        self.assertAlmostEqual(taken, possible_to_take)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_take_negative_amount(self):
        saldo_og = self.varasto.saldo
        taken = self.varasto.ota_varastosta(-1337)
        self.assertAlmostEqual(taken, 0)
        self.assertAlmostEqual(self.varasto.saldo, saldo_og)

    def test_str(self):
        self.assertEqual(str(self.varasto), "saldo = 0, vielä tilaa 10")
        
    def test_varasto_invalid_ctor_values(self):
        test_varasto = Varasto(-1337, -42)
        
        self.assertAlmostEqual(test_varasto.tilavuus, 0)
        self.assertAlmostEqual(test_varasto.saldo, 0)
    
    def test_varasto_ctor_invalid_saldo(self):
        test_varasto = Varasto(6, 9)
        self.assertAlmostEqual(test_varasto.saldo, 6)