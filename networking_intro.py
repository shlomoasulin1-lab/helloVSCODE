"""
🌐 מבוא ללמידת רשתות - Networking Introduction
=================================================
קובץ זה מדגים את המושגים הבסיסיים ברשתות מחשבים
"""

import socket
import json
from datetime import datetime

# ============================================================================
# 1. מושג: DNS - פתרון שמות (Domain Name System)
# ============================================================================
def resolve_domain(domain_name):
    """
    DNS תורגם שם דומיין לכתובת IP
    לדוגמה: google.com -> 142.250.xx.xx
    """
    print(f"\n🔍 חיפוש כתובת IP עבור: {domain_name}")
    try:
        ip_address = socket.gethostbyname(domain_name)
        print(f"✅ קיבלנו את ה-IP: {ip_address}")
        return ip_address
    except socket.gaierror as e:
        print(f"❌ שגיאה בחיפוש: {e}")
        return None


# ============================================================================
# 2. מושג: פתחים (Ports) - דרכים לתקשור
# ============================================================================
def get_common_ports():
    """
    פתחים הם "דלתות" שמאפשרות תקשור שונה:
    """
    common_ports = {
        80: "HTTP - אתרים רגילים",
        443: "HTTPS - אתרים מאובטחים",
        22: "SSH - גישה מרחוק מאובטחת",
        21: "FTP - העברת קבצים",
        25: "SMTP - שליחת אימייל",
        110: "POP3 - קבלת אימייל",
        3306: "MySQL - בסיס נתונים",
        5432: "PostgreSQL - בסיס נתונים"
    }
    
    print("\n🚪 פתחים נפוצים ברשתות:")
    print("=" * 50)
    for port, description in common_ports.items():
        print(f"  🔌 פתח {port:5d} ➜ {description}")
    
    return common_ports


# ============================================================================
# 3. מושג: סוקט (Socket) - נקודת קצה בתקשורת
# ============================================================================
def check_port_open(host, port):
    """
    בדיקה האם פתח מסוים פתוח בשרת
    """
    print(f"\n🔐 בדיקת פתח {port} בשרת {host}...")
    socket_obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_obj.settimeout(2)
    
    try:
        result = socket_obj.connect_ex((host, port))
        if result == 0:
            print(f"✅ פתח {port} פתוח! (השרת מגיב)")
        else:
            print(f"❌ פתח {port} סגור (אין תגובה)")
        return result == 0
    except Exception as e:
        print(f"⚠️  שגיאה: {e}")
    finally:
        socket_obj.close()


# ============================================================================
# 4. מושג: IP Address - כתובת רשת
# ============================================================================
def analyze_ip_address():
    """
    הבנת מבנה כתובות IP
    """
    print("\n📍 ניתוח כתובות IP:")
    print("=" * 50)
    
    examples = {
        "127.0.0.1": "Localhost - המחשב שלך עצמו",
        "192.168.1.1": "IP פרטית - משתמש בבית/חברה",
        "8.8.8.8": "DNS של Google - שרת ציבורי",
        "255.255.255.255": "Broadcast - שליחה לכולם ברשת"
    }
    
    for ip, description in examples.items():
        print(f"  🌐 {ip:15s} ➜ {description}")


# ============================================================================
# 5. מושג: פרוטוקול (Protocol) - כללים לתקשורת
# ============================================================================
def explain_protocols():
    """
    הסברת פרוטוקולים בתקשורת
    """
    print("\n📋 פרוטוקולים בתקשורת רשתות:")
    print("=" * 50)
    
    protocols = {
        "TCP": {
            "שם מלא": "Transmission Control Protocol",
            "תיאור": "מהימן - כל הנתונים מתקבלים בסדר",
            "דוגמה": "שליחת אימייל, גלישה באינטרנט"
        },
        "UDP": {
            "שם מלא": "User Datagram Protocol",
            "תיאור": "מהיר אך פחות מהימן - חלק מהנתונים עלול לאבוד",
            "דוגמה": "וידאו-שיחה, משחקים online"
        },
        "HTTP/HTTPS": {
            "שם מלא": "HyperText Transfer Protocol",
            "תיאור": "פרוטוקול בנוי על TCP - גלישה אתרים",
            "דוגמה": "דפים ברשת, API קריאות"
        }
    }
    
    for protocol, info in protocols.items():
        print(f"\n  🔗 {protocol}")
        print(f"     • {info['שם מלא']}")
        print(f"     • {info['תיאור']}")
        print(f"     • דוגמה: {info['דוגמה']}")


# ============================================================================
# 6. מושג: Model OSI - שכבות תקשורת
# ============================================================================
def osi_model():
    """
    מודל OSI - 7 שכבות בתקשורת רשתות
    """
    print("\n🏗️  מודל OSI - 7 שכבות בתקשורת:")
    print("=" * 50)
    
    layers = [
        ("1", "Physical", "כבלים, גלים רדיו"),
        ("2", "Data Link", "Switches, MAC Addresses"),
        ("3", "Network", "IP Addresses, Routers"),
        ("4", "Transport", "TCP, UDP"),
        ("5", "Session", "ניהול החיבורים"),
        ("6", "Presentation", "הצפנה, דחיסה"),
        ("7", "Application", "HTTP, SMTP, DNS")
    ]
    
    for level, name, description in layers:
        print(f"  📊 שכבה {level}: {name:15s} ➜ {description}")


# ============================================================================
# תוכנית ראשית
# ============================================================================
def main():
    print("\n" + "="*60)
    print("🎓 ברוכים הבאים ללמידת רשתות מחשבים!")
    print("="*60)
    print(f"⏰ תאריך: {datetime.now().strftime('%H:%M:%S %d/%m/%Y')}")
    print("="*60)
    
    # הרצת כל הפונקציות
    get_common_ports()
    analyze_ip_address()
    explain_protocols()
    osi_model()
    
    # בדיקה אם אתר פופולרי זמין
    resolve_domain("google.com")
    check_port_open("google.com", 443)
    
    print("\n" + "="*60)
    print("✨ סיימנו סיור בעולם הרשתות! לעוד ידע, המשך בלמידה!")
    print("="*60 + "\n")


if __name__ == "__main__":
    main()
