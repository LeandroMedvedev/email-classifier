from services.nlp_service import EmailClassifier

if __name__ == "__main__":
    classifier = EmailClassifier()

    email_exemplo = "Olá, gostaria de saber o status da minha solicitação de suporte."
    print("E-mail:", email_exemplo)
    print("Categoria:", classifier.classify(email_exemplo))
