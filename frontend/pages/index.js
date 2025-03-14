import { useEffect } from "react";
import { useRouter } from "next/router";

export default function Home() {
  const router = useRouter();

  useEffect(() => {
    router.push("/auth/splash"); // Redirige vers la page de splash screen
  }, []);

  return <div>Redirection en cours...</div>; // Affiche un message temporaire
}


