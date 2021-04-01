class UserCompanyAdapter:

    @staticmethod
    def to_json(results):
        return [
            {
                "company_id": user_company.company_id,
                "user_id": user_company.user_id
            } for user_company in results
        ]

    @staticmethod
    def to_single_json(company):
        return {
            "company_id": company.company_id,
            "user_id": company.user_id
        }

    def to_object(self, body):
        for key, value in body.items():
            if hasattr(self, key):
                setattr(self, key, value)
