import React, { useState } from "react";
import { Layout } from "antd";
import { UserOutlined, LogoutOutlined } from "@ant-design/icons";
import styles from "../styles/inscriptionprestataire.module.css";
import CustomFooter from "./Footer";

const { Header, Content } = Layout;

const InscriptionPrestataire = () => {
  const [formData, setFormData] = useState({
    fullName: "",
    companyName: "",
    siret: "",
    address: "",
    website: "",
    phone: "",
    email: "",
    expertise: [],
    certifications: [],
    languages: [],
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
      {/* HEADER */}
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
          <h2 className={styles.title}>
            Formulaire d'inscription pour prestataires
          </h2>

          <form onSubmit={handleSubmit} className={styles.form}>
            <section>
              <h3 className={styles.subtitle}>
                1. Informations sur l’entreprise
              </h3>
              <label className={styles.label}>Nom et Prénom</label>
              <input
                className={styles.input}
                type="text"
                name="fullName"
                onChange={handleChange}
              />

              <label className={styles.label}>
                Nom de l’entreprise (si applicable)
              </label>
              <input
                className={styles.input}
                type="text"
                name="companyName"
                onChange={handleChange}
              />

              <label className={styles.label}>
                Numéro SIRET / Identifiant fiscal
              </label>
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

              <label className={styles.label}>
                Site web / Portfolio professionnel
              </label>
              <input
                className={styles.input}
                type="text"
                name="website"
                onChange={handleChange}
              />

              <label className={styles.label}>Téléphone</label>
              <input
                className={styles.input}
                type="text"
                name="phone"
                onChange={handleChange}
              />

              <label className={styles.label}>
                Adresse e-mail professionnelle
              </label>
              <input
                className={styles.input}
                type="email"
                name="email"
                onChange={handleChange}
              />

              <label className={styles.label}>Photo de profil</label>
              <input className={styles.input} type="file" name="photo" />
            </section>

            <section>
              <h3 className={styles.subtitle}>2. Domaine d’Expertise</h3>
              <label className={styles.label}>Type de prestation</label>
              {[
                "Thérapie individuelle",
                "Coaching professionnel",
                "Bien-être",
                "Sport",
                "Conférences",
              ].map((exp) => (
                <div key={exp}>
                  <input
                    type="checkbox"
                    name="expertise"
                    value={exp}
                    onChange={handleChange}
                  />{" "}
                  {exp}
                </div>
              ))}

              <h3 className={styles.subtitle}>Expérience et certifications</h3>
              <label className={styles.label}>CV</label>
              <input className={styles.input} type="file" name="cv" />

              <label className={styles.label}>Diplôme</label>
              <input className={styles.input} type="file" name="diploma" />

              <label className={styles.label}>Certification</label>
              <input
                className={styles.input}
                type="file"
                name="certification"
              />
            </section>

            <section>
              <h3 className={styles.subtitle}>3. Connexion et Sécurité</h3>
              <label className={styles.label}>Créer un mot de passe</label>
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
              <h3 className={styles.subtitle}>4. Acceptation et validation</h3>
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

            <button type="submit" className={styles.submitButton}>
              Créer un compte
            </button>
          </form>
        </div>
      </Content>

      <CustomFooter />
    </Layout>
  );
};

export default InscriptionPrestataire;
