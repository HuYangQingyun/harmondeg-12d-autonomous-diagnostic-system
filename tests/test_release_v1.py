import unittest
from harmondeg12d_public import diagnose_text, make_template, load_dimensions_spec
from harmondeg12d_public.models import FRAMEWORK_VERSION, PACKAGE_VERSION

class ReleaseV1(unittest.TestCase):
    def test_versions(self):
        self.assertEqual(FRAMEWORK_VERSION, "Harmondeg 12-D Autonomous Diagnostic System v1.0")
        self.assertEqual(PACKAGE_VERSION, "1.0.0")
        self.assertEqual(diagnose_text("A proposition.")["framework_version"], FRAMEWORK_VERSION)

    def test_spec(self):
        spec=load_dimensions_spec()
        self.assertEqual(spec["framework_version"], FRAMEWORK_VERSION)
        self.assertEqual(spec["package_version"], PACKAGE_VERSION)

    def test_positive_gate(self):
        result=diagnose_text("Only within this case, the claim holds.")
        for value in result["dimensions"].values():
            if value["status"]=="scored" and value["score"]>0:
                self.assertTrue(value["active_management_evidence"])

    def test_self_reference_not_loop(self):
        self.assertEqual(diagnose_text("I examine my own thought.")["dimensions"]["D8"]["score"],0)

    def test_pure_theory_not_forced_into_practice(self):
        result=diagnose_text("Justice concerns institutions and may have effects.")
        self.assertEqual(result["dimensions"]["D11"]["status"],"N/A")
        self.assertEqual(result["dimensions"]["D12"]["status"],"N/A")

if __name__=="__main__":
    unittest.main()
