import React, { useState } from "react";
import { Layout } from "antd";
import { UserOutlined, LogoutOutlined } from "@ant-design/icons";
import styles from "../styles/inscriptionsociete.module.css";
import CustomFooter from "./Footer";

const { Header, Content } = Layout;

const InscriptionSociete = () => {
  const [formData, setFormData] = useState({
    companyName: "",
    siret: "",
    address: "",
    companySize: "",
    website: "",
    activitySector: "",
    legalRepName: "",
    legalRepFunction: "",
    phone: "",
    email: "",
    paymentMethod: "",
    accountHolder: "",
    iban: "",
    billingAddress: "",
    password: "",
    confirmPassword: "",
    acceptTerms: false,
    subscribeNewsletter: false,
  });

  const handleChange = (e) => {
    const { name, value, type, checked } = e.target;
    setFormData((prev) => ({
      ...prev,
      [name]: type === "checkbox" ? checked : value,
    }));
  };

  const handleLogout = () => {
    console.log("Déconnexion...");
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log(formData);
  };

  return (
    <Layout className={styles.layout}>
      <Header className={styles.adminHeader}>
        <div className={styles.leftSection}>
          <img src="/logo_alone.png" alt="Logo" className={styles.headerLogo} />
          <span className={styles.logoText}>CareConnect</span>
          <UserOutlined className={styles.icon} />
        </div>
        <div className={styles.rightSection}>
          <LogoutOutlined className={styles.icon} onClick={handleLogout} />
        </div>
      </Header>
      <Content className={styles.content}>
        <div className={styles.container}>
          <h2 className={styles.title}>Formulaire d'inscription</h2>
          <form onSubmit={handleSubmit} className={styles.form}>
            <section>
              <h3 className={styles.subtitle}>
                1. Informations sur l’entreprise
              </h3>

              <label className={styles.label}>Nom de la société</label>
              <input
                className={styles.input}
                type="text"
                name="companyName"
                onChange={handleChange}
              />

              <label className={styles.label}>Numéro SIRET</label>
              <input
                className={styles.input}
                type="text"
                name="siret"
                onChange={handleChange}
              />

              <label className={styles.label}>Adresse complète</label>
              <input
                className={styles.input}
                type="text"
                name="address"
                onChange={handleChange}
              />

              <label className={styles.label}>Effectif de l’entreprise</label>
              <div className={styles.radioGroup}>
                <button
                  type="button"
                  className={`${styles.radioButton} ${
                    formData.companySize === "1-30" ? styles.selected : ""
                  }`}
                  onClick={() =>
                    setFormData({ ...formData, companySize: "1-30" })
                  }
                >
                  1-30
                </button>
                <button
                  type="button"
                  className={`${styles.radioButton} ${
                    formData.companySize === "31-250" ? styles.selected : ""
                  }`}
                  onClick={() =>
                    setFormData({ ...formData, companySize: "31-250" })
                  }
                >
                  31-250
                </button>
                <button
                  type="button"
                  className={`${styles.radioButton} ${
                    formData.companySize === ">251" ? styles.selected : ""
                  }`}
                  onClick={() =>
                    setFormData({ ...formData, companySize: ">251" })
                  }
                >
                  {">"}251
                </button>
              </div>

              <label className={styles.label}>Site web de l’entreprise</label>
              <input
                className={styles.input}
                type="text"
                name="website"
                onChange={handleChange}
              />

              <label className={styles.label}>Secteur d’activité</label>
              <div className={styles.radioGroup}>
                {["Technologie", "Santé", "Commerce", "Autre"].map((sector) => (
                  <label key={sector} className={styles.radioLabel}>
                    <input
                      type="radio"
                      name="activitySector"
                      value={sector}
                      checked={formData.activitySector === sector}
                      onChange={handleChange}
                    />
                    {sector}
                  </label>
                ))}
              </div>
            </section>

            <section>
              <h3 className={styles.subtitle}>
                2. Informations du représentant légal
              </h3>

              <label className={styles.label}>Nom et prénom</label>
              <input
                className={styles.input}
                type="text"
                name="legalRepName"
                onChange={handleChange}
              />

              <label className={styles.label}>Fonction/Poste</label>
              <select
                className={styles.select}
                name="legalRepFunction"
                onChange={handleChange}
              >
                <option value="">Sélectionner</option>
                <option value="PDG">PDG</option>
                <option value="Manager RH">Manager RH</option>
                <option value="DRH">DRH</option>
                <option value="Autre">Autre</option>
              </select>

              <label className={styles.label}>Numéro de téléphone</label>
              <input
                className={styles.input}
                type="tel"
                name="phone"
                onChange={handleChange}
              />

              <label className={styles.label}>Email professionnel</label>
              <input
                className={styles.input}
                type="email"
                name="email"
                onChange={handleChange}
              />
            </section>

            <section>
              <h3 className={styles.subtitle}>3. Mode de paiement</h3>

              <label className={styles.label}>Méthode de paiement</label>
              <select
                className={styles.select}
                name="paymentMethod"
                onChange={handleChange}
              >
                <option value="">Sélectionner</option>
                <option value="Carte bancaire">Carte bancaire</option>
                <option value="Prélèvement SEPA">Prélèvement SEPA</option>
                <option value="Virement bancaire">Virement bancaire</option>
              </select>

              {formData.paymentMethod === "Carte bancaire" && (
                <>
                  <label className={styles.label}>
                    Nom du titulaire du compte
                  </label>
                  <input
                    className={styles.input}
                    type="text"
                    name="accountHolder"
                    onChange={handleChange}
                  />
                </>
              )}

              {formData.paymentMethod === "Prélèvement SEPA" && (
                <>
                  <label className={styles.label}>IBAN</label>
                  <input
                    className={styles.input}
                    type="text"
                    name="iban"
                    onChange={handleChange}
                  />
                </>
              )}

              {formData.paymentMethod === "Virement bancaire" && (
                <>
                  <label className={styles.label}>
                    Nom du titulaire du compte
                  </label>
                  <input
                    className={styles.input}
                    type="text"
                    name="accountHolder"
                    onChange={handleChange}
                  />

                  <label className={styles.label}>Adresse de facturation</label>
                  <input
                    className={styles.input}
                    type="text"
                    name="billingAddress"
                    onChange={handleChange}
                  />
                </>
              )}
            </section>

            <section>
              <h3 className={styles.subtitle}>5. Connexion et Sécurité</h3>

              <label className={styles.label}>
                Créer un mot de passe (8 caractères minimum)
              </label>
              <input
                className={styles.input}
                type="password"
                name="password"
                onChange={handleChange}
              />

              <label className={styles.label}>Confirmer le mot de passe</label>
              <input
                className={styles.input}
                type="password"
                name="confirmPassword"
                onChange={handleChange}
              />
            </section>

            <section>
              <h3 className={styles.subtitle}>6. Acceptation et validation</h3>

              <label className={styles.checkboxLabel}>
                <input
                  type="checkbox"
                  name="acceptTerms"
                  onChange={handleChange}
                />
                J'accepte les Conditions Générales d'Utilisation (CGU) et la
                Politique de confidentialité
              </label>

              <label className={styles.checkboxLabel}>
                <input
                  type="checkbox"
                  name="subscribeNewsletter"
                  onChange={handleChange}
                />
                Je souhaite recevoir des emails concernant les nouveautés et
                offres spéciales
              </label>
            </section>

            <button type="submit" className={styles.button}>
              Créer un compte
            </button>
          </form>
        </div>
      </Content>
      <CustomFooter />
    </Layout>
  );
};

export default InscriptionSociete;
