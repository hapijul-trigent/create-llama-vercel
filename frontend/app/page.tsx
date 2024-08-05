import Image from "next/image";
import Header from "./components/Header";
import TodoTable from "./components/TodoTable";

export default function Home() {
  return (
    <main className="flex min-h-screen flex-col items-center justify-between p-24">
      <div className="z-10 w-full max-w-5xl items-center justify-between font-mono text-sm lg:flex">
        <Header></Header>
        <TodoTable></TodoTable>
      </div>
    </main>
  );
}
