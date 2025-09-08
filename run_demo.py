#!/usr/bin/env python3
"""
Calculator Demo Launcher
========================

This script allows you to easily run and compare different modern calculator implementations:

1. Original Calculator (MobileCalc.py) - Modernized with custom styling
2. TTK Themes Calculator - Uses ttkthemes for professional styling
3. TTK Bootstrap Calculator - Uses ttkbootstrap for Bootstrap-style UI
4. CustomTkinter Calculator - Uses customtkinter for modern, sleek design

Each calculator offers different visual styles and features to showcase
modern UI design possibilities with Python GUI frameworks.
"""

import sys
import subprocess
import os
from pathlib import Path

class CalculatorLauncher:
    def __init__(self):
        self.calculators = {
            "1": {
                "name": "Original Modern Calculator",
                "file": "MobileCalc.py",
                "description": "Enhanced original calculator with modern colors and styling"
            },
            "2": {
                "name": "TTK Themes Calculator", 
                "file": "TTKThemesCalc.py",
                "description": "Professional calculator using ttkthemes (Arc theme)"
            },
            "3": {
                "name": "TTK Bootstrap Calculator",
                "file": "TTKBootstrapCalc.py", 
                "description": "Bootstrap-styled calculator with modern components"
            },
            "4": {
                "name": "CustomTkinter Calculator",
                "file": "CustomTkinterCalc.py",
                "description": "Sleek, modern calculator with rounded corners and smooth animations"
            },
            "5": {
                "name": "Modern Enhanced Calculator",
                "file": "ModernCalc.py",
                "description": "Feature-rich calculator with advanced functions and modern design"
            },
            "6": {
                "name": "Simple Modern Calculator",
                "file": "test.py",
                "description": "Simplified calculator with modern color scheme"
            }
        }
    
    def display_menu(self):
        print("=" * 70)
        print("🧮 MODERN CALCULATOR SHOWCASE")
        print("=" * 70)
        print()
        
        for key, calc in self.calculators.items():
            print(f"{key}. {calc['name']}")
            print(f"   📁 {calc['file']}")
            print(f"   📝 {calc['description']}")
            print()
        
        print("0. Exit")
        print()
        print("=" * 70)
    
    def check_dependencies(self, calculator_file):
        """Check if required dependencies are available"""
        dependencies = {
            "TTKThemesCalc.py": ["ttkthemes"],
            "TTKBootstrapCalc.py": ["ttkbootstrap"], 
            "CustomTkinterCalc.py": ["customtkinter"]
        }
        
        if calculator_file in dependencies:
            missing = []
            for dep in dependencies[calculator_file]:
                try:
                    __import__(dep)
                except ImportError:
                    missing.append(dep)
            
            if missing:
                print(f"❌ Missing dependencies: {', '.join(missing)}")
                print(f"   Install with: pip install {' '.join(missing)}")
                return False
        
        return True
    
    def run_calculator(self, calculator_file):
        """Run the selected calculator"""
        if not os.path.exists(calculator_file):
            print(f"❌ Calculator file not found: {calculator_file}")
            return
        
        if not self.check_dependencies(calculator_file):
            return
        
        print(f"🚀 Launching {calculator_file}...")
        print("   Press Ctrl+C to return to menu")
        print()
        
        try:
            # Run the calculator in a subprocess
            subprocess.run([sys.executable, calculator_file], check=True)
        except subprocess.CalledProcessError as e:
            print(f"❌ Error running calculator: {e}")
        except KeyboardInterrupt:
            print("\n⏹️  Calculator stopped by user")
        except Exception as e:
            print(f"❌ Unexpected error: {e}")
    
    def run(self):
        """Main launcher loop"""
        while True:
            try:
                self.display_menu()
                choice = input("Select a calculator to run (0-6): ").strip()
                
                if choice == "0":
                    print("👋 Thanks for trying the modern calculators!")
                    break
                
                if choice in self.calculators:
                    calc_info = self.calculators[choice]
                    print(f"\n🎯 Selected: {calc_info['name']}")
                    print("-" * 50)
                    self.run_calculator(calc_info['file'])
                    print("\n" + "=" * 50)
                    input("Press Enter to return to menu...")
                else:
                    print("❌ Invalid choice. Please select 0-6.")
                    input("Press Enter to continue...")
                
            except KeyboardInterrupt:
                print("\n\n👋 Goodbye!")
                break
            except Exception as e:
                print(f"❌ Error: {e}")
                input("Press Enter to continue...")

def main():
    """Main entry point"""
    print("🔧 Checking calculator files...")
    
    # Check if we're in the right directory
    required_files = ["MobileCalc.py", "test.py"]
    missing_files = [f for f in required_files if not os.path.exists(f)]
    
    if missing_files:
        print(f"❌ Missing required files: {', '.join(missing_files)}")
        print("   Make sure you're running this from the calculator directory")
        return
    
    print("✅ Calculator files found!")
    print()
    
    launcher = CalculatorLauncher()
    launcher.run()

if __name__ == "__main__":
    main()
