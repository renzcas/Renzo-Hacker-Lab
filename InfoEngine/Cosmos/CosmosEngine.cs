using System;
using Python.Runtime;

namespace InfoEngine.Cosmos
{
    /// <summary>
    /// Python-backed CosmosEngine stub.
    /// Manages dimensions, physics fields, and cosmos step cycles.
    /// </summary>
    public class CosmosEngine
    {
        private dynamic _dimensions;
        private dynamic _physicsEngine;

        public CosmosEngine()
        {
            // Ensure Python path includes the InfoEngine cosmos root
            Environment.SetEnvironmentVariable("PYTHONPATH", "/workspaces/Renzo-Hacker-Lab/InfoEngine");

            PythonEngine.Initialize();

            using (Py.GIL())
            {
                // Import Python cosmos modules
                _dimensions   = Py.Import("Cosmos.Dimensions");
                _physicsEngine = Py.Import("Cosmos.Physics.dynamics");
            }

            Console.WriteLine("[CosmosEngine] Python cosmos modules initialized.");
        }

        ~CosmosEngine()
        {
            PythonEngine.Shutdown();
        }

        // ---------------------------------------------------------------------
        // Cosmos Step Cycle
        // ---------------------------------------------------------------------
        public void Step(double dt)
        {
            using (Py.GIL())
            {
                // Call python-backed physics/cosmos step if available
                if (_physicsEngine.HasAttr("step"))
                {
                    _physicsEngine.step(dt);
                }
            }
        }

        // ---------------------------------------------------------------------
        // Dimension / Scaling Utilities
        // ---------------------------------------------------------------------
        public double ComputeEnergyScale(double mass, double velocity)
        {
            using (Py.GIL())
            {
                dynamic dimsInstance = _dimensions.Dimensions();
                return dimsInstance.energy_scale(mass, velocity).As<double>();
            }
        }
    }
}