// GOAT buy/sell engine — verified against BUY_SELL_TOOL.xlsx and the MVP.
export type Ratings = {
  rookie: number;   // rookie / chase strength 1-5
  scarcity: number; // print run / scarcity 1-5
  brand: number;    // brand tier 1-5
  velocity: number; // sales velocity / liquidity 1-5
  hype: number;     // hype / catalyst 1-5
};

export type Verdict = "BUY-FLIP" | "BUY-HOLD" | "PASS" | "WATCH/THIN";

export type BuyResult = {
  net: number;
  margin: number;
  roi: number;
  score: number;
  verdict: Verdict;
};

export function scoreBuy(
  retail: number,
  comp: number,
  feePct: number,
  perOrder: number,
  r: Ratings
): BuyResult {
  const net = comp * (1 - feePct) - perOrder;
  const margin = net - retail;
  const roi = retail > 0 ? margin / retail : 0;
  const sum = r.rookie + r.scarcity + r.brand + r.velocity + r.hype;
  const score = Math.round(
    Math.min(40, Math.max(0, roi * 80)) + (sum / 25) * 60
  );
  let verdict: Verdict;
  if (roi < 0.05 && sum / 5 < 3.5) verdict = "PASS";
  else if ((r.rookie + r.scarcity) / 2 >= 4) verdict = "BUY-HOLD";
  else if (roi >= 0.25 && r.velocity >= 3) verdict = "BUY-FLIP";
  else verdict = "WATCH/THIN";
  return { net, margin, roi, score, verdict };
}

export type SellResult = {
  months: number;
  phase: string;
  gain: number;
  action: string;
};

export function sellTiming(
  releaseISO: string,
  cost: number,
  comp: number,
  mult: number
): SellResult {
  const t = new Date();
  const rel = new Date(releaseISO);
  const months =
    (t.getFullYear() - rel.getFullYear()) * 12 + (t.getMonth() - rel.getMonth());
  const phase =
    months < 0
      ? "1 Pre-release"
      : months < 6
      ? "2 Launch"
      : months < 24
      ? "3 Saturation"
      : months < 60
      ? "4 Consolidation"
      : "5 Scarcity";
  const gain = cost > 0 ? (comp - cost) / cost : 0;
  let action: string;
  if (mult && comp && comp >= cost * mult) action = "SELL — target hit";
  else if (phase[0] === "5") action = "SELL WINDOW (yr 5-7)";
  else if (phase[0] === "4") action = "Take partial / hold";
  else if (phase[0] === "1") action = "Avoid / flip only";
  else action = "ACCUMULATE / hold";
  return { months, phase, gain, action };
}

export type GradeResult = {
  rawNet: number;
  gradedNet: number;
  delta: number;
  verdict: "GRADE IT" | "MARGINAL" | "SELL RAW";
};

export function gradeOrSell(
  raw: number,
  psa10: number,
  gradeCost: number,
  feePct: number
): GradeResult {
  const rawNet = raw * (1 - feePct);
  const gradedNet = psa10 * (1 - feePct) - gradeCost;
  const delta = gradedNet - rawNet;
  let verdict: GradeResult["verdict"];
  if (delta >= 20) verdict = "GRADE IT";
  else if (delta > 0) verdict = "MARGINAL";
  else verdict = "SELL RAW";
  return { rawNet, gradedNet, delta, verdict };
}
