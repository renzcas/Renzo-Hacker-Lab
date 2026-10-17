using System;
using Renzoverse.DivineMath;
using InfoEngine.Cosmos;
using InfoEngine.Interop;

namespace InfoEngine
{
    /// <summary>
    /// Unified InfoEngine:
    /// - Cosmos (math, physics, monads, interaction)
    /// - Cyber (cockpit, agents, tools)
    /// - Interop (Python ↔ C#, Renzoverse bridges)
    /// </summary>
    public class InfoEngineCore
    {
        // Cosmos
        private readonly CosmosEngine _cosmos;
        private readonly DivineMathEngine _divineMath;

        // Interop
        private readonly LineageBridge _lineage;
        private readonly FlowBridge _flow;
        private readonly StateBridge _state;
        private readonly SurgeryBridge _surgery;

        public InfoEngineCore()
        {
            Console.WriteLine("[InfoEngine] Booting unified engine...");

            // Cosmos
            _cosmos     = new CosmosEngine();
            _divineMath = new DivineMathEngine();

            // Interop
            _lineage = new LineageBridge();
            _flow    = new FlowBridge();
            _state   = new StateBridge();
            _surgery = new SurgeryBridge();

            Console.WriteLine("[InfoEngine] Cosmos + Interop online.");
        }

        // ---------------------------------------------------------------------
        // High-level API for Renzoverse / CaveSharp-OS
        // ---------------------------------------------------------------------

        public string GetLineage(string id) =>
            _lineage.GetLineage(id);

        public string GetFlowStep(string cycleId) =>
            _flow.Step(cycleId);

        public string GetArchetypeState(string archetypeId) =>
            _state.GetState(archetypeId);

        public string ApplySymbolicSurgery(string symbol) =>
            _surgery.Transform(symbol);

        public double HilbertMode(double x) =>
            _divineMath.HilbertMode(x);

        public double RiemannField(double x) =>
            _divineMath.RiemannField(x);

        public double RicciFlow(double x) =>
            _divineMath.RicciFlow(x);

        public double PerelmanEntropy(double x) =>
            _divineMath.PerelmanEntropy(x);

        // Example cosmos tick
        public void Tick(double dt)
        {
            _cosmos.Step(dt);
        }
    }
}