import { useState, useEffect } from "react";
import { Layout, Table, Tabs, Button } from "antd";
import {
  EyeOutlined,
  UserOutlined,
  SearchOutlined,
  LogoutOutlined,
  EditOutlined,
  DeleteOutlined,
  PlusCircleOutlined,
} from "@ant-design/icons";

const { Header, Content } = Layout;
const { TabPane } = Tabs;

const images = [
  "/healthcare.webp",
  "/headimage.jpg",
  "/webinars.jpeg",
  "/yoga.webp",
];

const ImageCarousel = () => {
  const [currentIndex, setCurrentIndex] = useState(0);

  useEffect(() => {
    const interval = setInterval(() => {
      setCurrentIndex((prevIndex) => (prevIndex + 1) % images.length);
    }, 5000);

    return () => clearInterval(interval);
  }, []);

  const goToImage = (index) => {
    setCurrentIndex(index);
  };

  return (
    <div className="carousel-container">
      <img
        src={images[currentIndex]}
        alt="carousel"
        className="carousel-image"
      />

      <div className="carousel-indicators">
        {images.map((_, index) => (
          <span
            key={index}
            className={`indicator ${index === currentIndex ? "active" : ""}`}
            onClick={() => goToImage(index)}
          ></span>
        ))}
      </div>
    </div>
  );
};

const Dashboard = () => {
  const [activeTab, setActiveTab] = useState("prestataire");

  const [stats, setStats] = useState({
    prestataire: 0,
    collaborateurs: 0,
    associations: 0,
    societes: 0,
    forums: 0,
    factures: 0,
  });

  const tabTitleMap = {
    prestataire: `PRESTATAIRE (${stats.prestataire})`,
    collaborateurs: `COLLABORATEURS (${stats.collaborateurs})`,
    associations: `ASSOCIATIONS (${stats.associations})`,
    societes: `SOCIÉTÉS (${stats.societes})`,
    forums: `FORUM (${stats.forums})`,
    factures: `FACTURES (${stats.factures})`,
  };

  const incrementStat = () => {
    setStats((prevStats) => ({
      ...prevStats,
      [activeTab]: prevStats[activeTab] + 1,
    }));
  };

  const handleEdit = (record) => {
    console.log("Modifier:", record);
  };

  const handleDelete = (record) => {
    console.log("Supprimer:", record);
  };

  const handleView = (record) => {
    console.log("Voir détails:", record);
  };

  const handleAddEvent = (record) => {
    console.log("Ajouter un événement pour:", record);
  };

  const dataByTab = {
    prestataire: [
      {
        key: "1",
        ref: "A001",
        name: "AAAA",
        date: "XX/XX/XXXX",
        status: "En attente",
      },
      {
        key: "2",
        ref: "A002",
        name: "BBBB",
        date: "XX/XX/XXXX",
        status: "Validé",
      },
      {
        key: "3",
        ref: "A003",
        name: "CCCC",
        date: "XX/XX/XXXX",
        status: "En attente",
      },
    ],
    collaborateurs: [
      {
        key: "1",
        ref: "A001",
        name: "AAAA",
        date: "XX/XX/XXXX",
        societes: "SOC_01",
      },
      {
        key: "2",
        ref: "A002",
        name: "BBBB",
        date: "XX/XX/XXXX",
        societes: "SOC_02",
      },
      {
        key: "3",
        ref: "A003",
        name: "CCCC",
        date: "XX/XX/XXXX",
        societes: "SOC_03",
      },
    ],
    societes: [
      {
        key: "1",
        ref: "A001",
        name: "SOC_01",
        date: "XX/XX/XXXX",
        email: "soc_01@gmail.com",
      },
      {
        key: "2",
        ref: "A002",
        name: "SOC_02",
        date: "XX/XX/XXXX",
        email: "soc_02@gmail.com",
      },
      {
        key: "3",
        ref: "A003",
        name: "SOC_03",
        date: "XX/XX/XXXX",
        email: "soc_03@gmail.com",
      },
    ],
    associations: [
      { key: "1", ref: "A001", name: "SOC_01", date: "XX/XX/XXXX" },
      { key: "2", ref: "A002", name: "SOC_02", date: "XX/XX/XXXX" },
      { key: "3", ref: "A003", name: "SOC_03", date: "XX/XX/XXXX" },
    ],
    forums: [
      {
        key: "1",
        ref: "A001",
        name: "Forum01",
        date: "XX/XX/XXXX",
        status: "passé",
      },
      {
        key: "2",
        ref: "A002",
        name: "Forum02",
        date: "XX/XX/XXXX",
        status: "A venir",
      },
      {
        key: "3",
        ref: "A003",
        name: "Forum03",
        date: "XX/XX/XXXX",
        status: "A venir",
      },
    ],
    factures: [
      {
        key: "1",
        ref: "A001",
        societe: "SOC_01",
        collaborateur: "COLL_01",
        date: "XX/XX/XXXX",
        status: "réglée",
      },
      {
        key: "2",
        ref: "A002",
        societe: "SOC_02",
        collaborateur: "COLL_02",
        date: "XX/XX/XXXX",
        status: "En attente",
      },
      {
        key: "3",
        ref: "A003",
        societe: "SOC_03",
        collaborateur: "COLL_03",
        date: "XX/XX/XXXX",
        status: "En attente",
      },
    ],
  };

  const columnsByTab = {
    prestataire: [
      { title: "Ref", dataIndex: "ref", key: "ref" },
      { title: "Nom", dataIndex: "name", key: "name" },
      { title: "Date", dataIndex: "date", key: "date" },
      { title: "Statut", dataIndex: "status", key: "status" },
      {
        title: "Modifier",
        key: "edit",
        render: (text, record) => (
          <Button
            type="link"
            icon={<EditOutlined />}
            onClick={() => handleEdit(record)}
          />
        ),
      },
      {
        title: "Supprimer",
        key: "delete",
        render: (text, record) => (
          <Button
            type="link"
            icon={<DeleteOutlined />}
            danger
            onClick={() => handleDelete(record)}
          />
        ),
      },
    ],
    collaborateurs: [
      { title: "Ref", dataIndex: "ref", key: "ref" },
      { title: "Nom", dataIndex: "name", key: "name" },
      { title: "Date", dataIndex: "date", key: "date" },
      { title: "Sociétés", dataIndex: "societes", key: "societes" },
      {
        title: "Voir",
        key: "view",
        render: (text, record) => (
          <Button
            type="link"
            icon={<EyeOutlined />}
            onClick={() => handleView(record)}
          />
        ),
      },
      {
        title: "Supprimer",
        key: "delete",
        render: (text, record) => (
          <Button
            type="link"
            icon={<DeleteOutlined />}
            danger
            onClick={() => handleDelete(record)}
          />
        ),
      },
    ],
    societes: [
      { title: "Ref", dataIndex: "ref", key: "ref" },
      { title: "Nom", dataIndex: "name", key: "name" },
      { title: "Date", dataIndex: "date", key: "date" },
      {
        title: "Contacter",
        dataIndex: "email",
        key: "email",
        render: (email) => <span>{email}</span>,
      },
      {
        title: "Voir",
        key: "view",
        render: (text, record) => (
          <Button
            type="link"
            icon={<EyeOutlined />}
            onClick={() => handleView(record)}
          />
        ),
      },
      {
        title: "Supprimer",
        key: "delete",
        render: (text, record) => (
          <Button
            type="link"
            icon={<DeleteOutlined />}
            danger
            onClick={() => handleDelete(record)}
          />
        ),
      },
    ],
    associations: [
      { title: "Ref", dataIndex: "ref", key: "ref" },
      { title: "Nom", dataIndex: "name", key: "name" },
      { title: "Date", dataIndex: "date", key: "date" },
      {
        title: "Voir",
        key: "view",
        render: (text, record) => (
          <Button
            type="link"
            icon={<EyeOutlined />}
            onClick={() => handleView(record)}
          />
        ),
      },
      {
        title: "Events",
        key: "events",
        render: (text, record) => (
          <Button
            type="link"
            icon={<PlusCircleOutlined />}
            onClick={() => handleAddEvent(record)}
          />
        ),
      },
      {
        title: "Supprimer",
        key: "delete",
        render: (text, record) => (
          <Button
            type="link"
            icon={<DeleteOutlined />}
            danger
            onClick={() => handleDelete(record)}
          />
        ),
      },
    ],
    forums: [
      { title: "Ref", dataIndex: "ref", key: "ref" },
      { title: "Nom", dataIndex: "name", key: "name" },
      { title: "Date", dataIndex: "date", key: "date" },
      {
        title: "Voir",
        key: "view",
        render: (text, record) => (
          <Button
            type="link"
            icon={<EyeOutlined />}
            onClick={() => handleView(record)}
          />
        ),
      },
      {
        title: "Statut",
        dataIndex: "status",
        key: "status",
        render: (status) => (
          <span
            style={{
              color: status === "passé" ? "red" : "green",
              fontWeight: "bold",
            }}
          >
            {status}
          </span>
        ),
      },
      {
        title: "Supprimer",
        key: "delete",
        render: (text, record) => (
          <Button
            type="link"
            icon={<DeleteOutlined />}
            danger
            onClick={() => handleDelete(record)}
          />
        ),
      },
    ],
    factures: [
      { title: "Ref", dataIndex: "ref", key: "ref" },
      { title: "Nom Société", dataIndex: "societe", key: "societe" },
      {
        title: "Collaborateur",
        dataIndex: "collaborateur",
        key: "collaborateur",
      },
      { title: "Date", dataIndex: "date", key: "date" },
      {
        title: "Voir",
        key: "view",
        render: (text, record) => (
          <Button
            type="link"
            icon={<EyeOutlined />}
            onClick={() => handleView(record)}
          />
        ),
      },
      {
        title: "Statut",
        dataIndex: "status",
        key: "status",
        render: (status) => (
          <span
            style={{
              color: status === "réglée" ? "red" : "green",
              fontWeight: "bold",
            }}
          >
            {status}
          </span>
        ),
      },
    ],
  };

  const handleLogout = () => {
    console.log("Déconnexion...");
  };

  return (
    <Layout className="dashboard-layout">
      <Header className="admin-header">
        <div className="left-section">
          <img src="/logo_alone.png" alt="Logo" className="header-logo" />
          <span className="logo-text">CareConnect</span>
          <UserOutlined className="icon profile-icon" />
        </div>

        <div className="center-section">
          <input
            type="text"
            placeholder="Rechercher..."
            className="search-bar"
          />
          <SearchOutlined className="icon" />
        </div>

        <div className="right-section">
          <LogoutOutlined className="icon logout-icon" onClick={handleLogout} />
        </div>
      </Header>

      <Content className="admin-content">
        <ImageCarousel />

        <Tabs activeKey={activeTab} onChange={setActiveTab} type="card">
          {Object.keys(tabTitleMap).map((tab) => (
            <TabPane tab={tabTitleMap[tab]} key={tab}>
              <Table
                columns={columnsByTab[tab] || []}
                dataSource={dataByTab[tab] || []}
                pagination={false}
              />
            </TabPane>
          ))}
        </Tabs>

        <Button type="primary" className="add-button" onClick={incrementStat}>
          Ajouter un {tabTitleMap[activeTab].split(" ")[0]}
        </Button>
      </Content>

      <footer className="admin-footer">
        &copy; {new Date().getFullYear()} Mon Dashboard - Tous droits réservés
      </footer>
    </Layout>
  );
};

export default Dashboard;
