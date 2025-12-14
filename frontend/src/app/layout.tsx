import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "Wikipedia Search",
  description: "Search through Wikipedia articles using our custom search engine",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body>
        {children}
      </body>
    </html>
  );
}
