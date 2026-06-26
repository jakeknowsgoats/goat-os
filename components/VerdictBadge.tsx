export function verdictClass(v: string): string {
  if (v.includes("FLIP")) return "bg-green-500/15 text-green-300 border border-green-700";
  if (v.includes("HOLD")) return "bg-blue-500/15 text-blue-300 border border-blue-700";
  if (v.includes("PASS") || v.includes("SELL")) return "bg-red-500/15 text-red-300 border border-red-800";
  return "bg-yellow-500/15 text-yellow-300 border border-yellow-700";
}

export default function VerdictBadge({ verdict }: { verdict: string }) {
  return (
    <span
      className={`inline-block rounded-lg px-4 py-2 text-lg font-extrabold ${verdictClass(
        verdict
      )}`}
    >
      {verdict}
    </span>
  );
}
