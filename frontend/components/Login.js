import { useState } from "react";
import { useRouter } from "next/router";
import { Layout } from "antd";
import { UserOutlined, LogoutOutlined } from "@ant-design/icons";
import styles from "../styles/auth.module.css";
import CustomFooter from "./Footer";

const { Header, Content } = Layout;
export default function Login() {
  const router = useRouter();
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const handleLogin = (e) => {
    e.preventDefault();
    console.log("Connexion avec :", email, password);
  };

  const handleLogout = () => {
    console.log("Déconnexion...");
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
        <div className={styles.loginContainer}>
          <div className={styles.loginBox}>
            <h2>Connexion</h2>
            <form onSubmit={handleLogin} className={styles.loginForm}>
              <div className={styles.formGroup}>
                <label className={styles.label}>
                  Nom d’utilisateur / Adresse mail :
                </label>
                <input
                  type="email"
                  className={styles.input}
                  placeholder="Nom d'utilisateur / Email"
                  value={email}
                  onChange={(e) => setEmail(e.target.value)}
                  required
                />
              </div>
              <div className={styles.formGroup}>
                <label className={styles.label}>Mot de passe :</label>
                <input
                  type="password"
                  className={styles.input}
                  placeholder="Mot de passe"
                  value={password}
                  onChange={(e) => setPassword(e.target.value)}
                  required
                />
              </div>
              <button type="submit" className={styles.loginButton}>
                Connexion
              </button>
            </form>
            <p className={styles.createAccount}>
              C'est votre première connexion ?{" "}
              <a href="/auth/usertype">Créer un compte</a>
            </p>
          </div>
        </div>
      </Content>
      <CustomFooter />
    </Layout>
  );
}
