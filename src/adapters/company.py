class CompanyAdapter:

    @staticmethod
    def to_json(results):
        return [
            {
                "id": company.id,
                "name": company.name,
                "street": company.street,
                "city": company.city,
                "country": company.country
            } for company in results
        ]

    @staticmethod
    def to_single_json(company):
        return {
            "id": company.id,
            "name": company.name,
            "street": company.street,
            "city": company.city,
            "country": company.country
        }

    def to_object(self, body):
        for key, value in body.items():
            if hasattr(self, key):
                setattr(self, key, value)


