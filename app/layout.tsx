import "./globals.css";
import type { Metadata } from "next";

export const metadata: Metadata = {
  title: "The Goat Monitor — Collector OS",
  description:
    "Drops, buy/sell intelligence, and your collection — in one place. 🐐",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body className="min-h-screen bg-bg text-[#e7e9ee] antialiased">
        {children}
      </body>
    </html>
  );
}
