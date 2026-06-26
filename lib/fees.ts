// Marketplace fees: [feePct, perOrder$]. Edit when rates change.
export const FEES: Record<string, [number, number]> = {
  "eBay": [0.136, 0.4],
  "eBay $1k+ promo": [0.068, 0.4],
  "TCGplayer": [0.1075, 0],
  "Whatnot": [0.095, 0],
  "PayPal G&S": [0.0349, 0.49],
  "Local / Cash": [0, 0],
  "Server BST": [0, 0],
};

export const MARKETPLACES = Object.keys(FEES);
