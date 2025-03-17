import { useState } from "react";
import styles from "../styles/inscriptionsalarie.module.css";
import { Layout } from "antd";
import { UserOutlined, LogoutOutlined } from "@ant-design/icons";
import CustomFooter from "./Footer";

const { Header, Content } = Layout;

export default function InscriptionSalarie() {
  const [form, setForm] = useState({
    nom: "",
    email: "",
    telephone: "",
    adresse: "",
    langue: "",
    services: [],
    horaire: "",
    password: "",
    confirmPassword: "",
    notifications: [],
    acceptCGU: false,
    newsletter: false,
  });

  const handleChange = (e) => {
    const { name, value, type, checked } = e.target;
    if (type === "checkbox") {
      if (name === "services" || name === "notifications") {
        setForm({
          ...form,
          [name]: checked
            ? [...form[name], value]
            : form[name].filter((item) => item !== value),
        });
      } else {
        setForm({ ...form, [name]: checked });
      }
    } else {
      setForm({ ...form, [name]: value });
    }
  };

  const handleLogout = () => {
    console.log("Déconnexion...");
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    if (form.password !== form.confirmPassword) {
      alert("Les mots de passe ne correspondent pas");
      return;
    }
    console.log("Données soumises:", form);
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
          <h2>Formulaire d'inscription</h2>
          <form onSubmit={handleSubmit} className={styles.form}>
            <section>
              <h3 className={styles.subtitle}>
                1. Informations sur l’entreprise
              </h3>
              <label className={styles.label}>Nom</label>
              <input
                className={styles.input}
                type="text"
                name="nom"
                onChange={handleChange}
              />

              <label className={styles.label}>Prénom</label>
              <input
                className={styles.input}
                type="text"
                name="prenom"
                onChange={handleChange}
              />

              <label className={styles.label}>Adresse complète</label>
              <input
                className={styles.input}
                type="text"
                name="adresse"
                onChange={handleChange}
              />

              <label className={styles.label}>Téléphone</label>
              <input
                className={styles.input}
                type="text"
                name="telephone"
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
            </section>

            <section>
              <h3 className={styles.subtitle}>2. Accès aux Services</h3>
              <label className={styles.label}>
                Types de services souhaités
              </label>
              <div className={styles.checkboxGroup}>
                <label>
                  <input
                    type="checkbox"
                    name="services"
                    value="Coaching"
                    onChange={handleChange}
                  />{" "}
                  Coaching professionnel
                </label>
                <label>
                  <input
                    type="checkbox"
                    name="services"
                    value="Bien-être mental"
                    onChange={handleChange}
                  />{" "}
                  Bien-être mental
                </label>
                <label>
                  <input
                    type="checkbox"
                    name="services"
                    value="Sport"
                    onChange={handleChange}
                  />{" "}
                  Activités sportives
                </label>
                <label>
                  <input
                    type="checkbox"
                    name="services"
                    value="Team-building"
                    onChange={handleChange}
                  />{" "}
                  Événements d'équipe
                </label>
                <label>
                  <input
                    type="checkbox"
                    name="services"
                    value="Webinaires"
                    onChange={handleChange}
                  />{" "}
                  Formations et webinaires
                </label>
              </div>
            </section>

            <section>
              <h3 className={styles.subtitle}>3. Connexion et Sécurité</h3>
              <label className={styles.label}>Mot de passe</label>
              <input
                type="password"
                name="password"
                className={styles.input}
                onChange={handleChange}
              />

              <label className={styles.label}>Confirmer le mot de passe</label>
              <input
                type="password"
                name="confirmPassword"
                className={styles.input}
                onChange={handleChange}
              />

              <label className={styles.label}>Notifications par :</label>
              <div className={styles.checkboxGroup}>
                <label>
                  <input
                    type="checkbox"
                    name="notifications"
                    value="Email"
                    onChange={handleChange}
                  />{" "}
                  Email
                </label>
                <label>
                  <input
                    type="checkbox"
                    name="notifications"
                    value="SMS"
                    onChange={handleChange}
                  />{" "}
                  SMS
                </label>
                <label>
                  <input
                    type="checkbox"
                    name="notifications"
                    value="Application"
                    onChange={handleChange}
                  />{" "}
                  Application mobile
                </label>
              </div>
            </section>

            <section>
              <h3 className={styles.subtitle}>4. Acceptation et validation</h3>
              <label className={styles.checkboxLabel}>
                <input
                  type="checkbox"
                  name="acceptCGU"
                  onChange={handleChange}
                />{" "}
                J'accepte les CGU
              </label>
              <label className={styles.checkboxLabel}>
                <input
                  type="checkbox"
                  name="newsletter"
                  onChange={handleChange}
                />{" "}
                Recevoir les offres spéciales
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
}
