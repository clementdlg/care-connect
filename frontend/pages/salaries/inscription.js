import dynamic from "next/dynamic";

const InscriptionSalarie = dynamic(
  () => import("../../components/inscriptionsalarie"),
  { ssr: false }
);

export default function SalariesPage() {
  return <InscriptionSalarie />;
}
