import { useEffect, useState } from "react";
import { PieChart, Pie, Cell, ResponsiveContainer, BarChart, Bar, XAxis, YAxis, Tooltip } from "recharts";

export default function App() {
  const [report, setReport] = useState({
    total_players: 100,
    cheat_players: 37,
    average_reaction_ms: 169.44,
    cheat_ratio_percent: 37,
  });

  useEffect(() => {
    fetch("http://127.0.0.1:8000/report")
      .then((res) => res.json())
      .then((data) => setReport(data))
      .catch(() => {});
  }, []);

  const safePlayers = report.total_players - report.cheat_players;
  const pieData = [
    { name: "정상", value: safePlayers },
    { name: "핵 의심", value: report.cheat_players },
  ];

  const barData = [
    { name: "반응속도", value: report.average_reaction_ms },
    { name: "핵비율", value: report.cheat_ratio_percent },
  ];

  const risk = report.cheat_ratio_percent >= 40 ? "HIGH" : report.cheat_ratio_percent >= 20 ? "MEDIUM" : "LOW";

  return (
    <div style={{ minHeight: "100vh", background: "#09090b", color: "white", padding: 32 }}>
      <div style={{ maxWidth: 1400, margin: "0 auto" }}>
        <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center", marginBottom: 24 }}>
          <h1 style={{ fontSize: 48, fontWeight: 700, margin: 0 }}>🎯 Anti-Cheat Command Center</h1>
          <div style={{ padding: "10px 16px", borderRadius: 999, border: "1px solid #ef4444", color: "#fca5a5" }}>
            Risk Level: {risk}
          </div>
        </div>

        <div style={{ display: "grid", gridTemplateColumns: "repeat(4, 1fr)", gap: 20, marginBottom: 30 }}>
          {[
            ["총 플레이어", report.total_players],
            ["핵 의심", report.cheat_players],
            ["평균 반응", `${report.average_reaction_ms} ms`],
            ["핵 비율", `${report.cheat_ratio_percent}%`],
          ].map(([title, value], idx) => (
            <div key={idx} style={{ background: "#18181b", padding: 24, borderRadius: 24, border: "1px solid #27272a" }}>
              <div style={{ color: "#a1a1aa", fontSize: 14 }}>{title}</div>
              <div style={{ fontSize: 36, fontWeight: 700, marginTop: 10 }}>{value}</div>
            </div>
          ))}
        </div>

        <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: 24 }}>
          <div style={{ background: "#18181b", padding: 24, borderRadius: 24, height: 420 }}>
            <h2 style={{ fontSize: 28, marginBottom: 16 }}>핵 비율 분포</h2>
            <ResponsiveContainer width="100%" height="85%">
              <PieChart>
                <Pie data={pieData} dataKey="value" outerRadius={120} label>
                  <Cell fill="#22c55e" />
                  <Cell fill="#ef4444" />
                </Pie>
                <Tooltip />
              </PieChart>
            </ResponsiveContainer>
          </div>

          <div style={{ background: "#18181b", padding: 24, borderRadius: 24, height: 420 }}>
            <h2 style={{ fontSize: 28, marginBottom: 16 }}>실시간 분석 지표</h2>
            <ResponsiveContainer width="100%" height="85%">
              <BarChart data={barData}>
                <XAxis dataKey="name" stroke="#a1a1aa" />
                <YAxis stroke="#a1a1aa" />
                <Tooltip />
                <Bar dataKey="value" fill="#ef4444" />
              </BarChart>
            </ResponsiveContainer>
          </div>
        </div>
      </div>
    </div>
  );
}
