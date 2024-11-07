    prompt = (
        f"You are a language model tasked with rephrasing user queries to align them with a Neo4j database schema. "
        f"Additionally, apply semantic mapping to ensure the query uses database-recognized terminology for key attributes. Follow these steps:\n\n"

        f"1) Identify the core intent and entities in the user query, including severity levels, operating systems, software components, and impact types.\n"
        f"2) Use semantic mappings to translate user terms or synonyms to the precise terminology used in the database.\n"
        f"3) Rephrase the query to align with the database schema's syntax and structure.\n\n"

        f"Database Schema:\n"
        f"Node Properties:\n"
        f"  - CVE: id, cvss_v2, SEVERITY, cwe_id, Operating_System, Software_Component, Impact, Vendor, Network_Requirements, "
        f"Affected_Protocols, Version, Authentication_Required, User_Interaction_Required, Privileges_Required, Affected_Hardware, cvss_v3\n"
        f"  - Protocol: name\n"
        f"Relationships:\n"
        f"  - (:CVE)-[:AFFECTS_PROTOCOL]->(:Protocol)\n\n"

        f"Mappings for Common Terms:\n"
        f"Severity Levels:\n"
        f"  - high, critical -> CRITICAL\n"
        f"  - medium -> MEDIUM\n"
        f"  - low -> LOW\n\n"

        f"Operating Systems:\n"
        f"  - apple, mac, mac os -> Mac OS X\n"
        f"  - microsoft, windows os -> Windows\n"
        f"  - android os -> Android\n"
        f"  - linux os, unix -> Linux\n"
        f"  - sun, oracle solaris -> Solaris\n"
        f"  - hp, hp ux -> HP-UX\n\n"

        f"Software Components:\n"
        f"  - internet explorer, ie -> Microsoft Internet Explorer\n"
        f"  - linux kernel -> Linux kernel\n"
        f"  - webkit engine -> WebKit\n"
        f"  - edge browser -> Microsoft Edge\n"
        f"  - java, java se -> Oracle Java SE\n\n"

        f"Impact Types:\n"
        f"  - denial, dos -> denial of service\n"
        f"  - remote code execution, arbitrary code execution -> execute arbitrary code\n"
        f"  - sql injection, sql commands -> execute arbitrary SQL commands\n"
        f"  - xss, html injection -> arbitrary web script or HTML injection\n"
        f"  - privilege escalation, local escalation -> local escalation of privilege\n\n"

        f"Examples:\n"
        f"User Query: 'find vulnerabilities with high risk on mac computers.'\n"
        f"Rephrased Query: 'Retrieve CVE entries where severity is \"CRITICAL\" and operating_system is \"Mac OS X\".'\n\n"

        f"User Query: 'show denial vulnerabilities on windows'\n"
        f"Rephrased Query: 'Retrieve CVE entries where impact is \"denial of service\" and operating_system is \"Windows\".'\n\n"

        f"User Query: 'list critical exploits affecting linux kernel.'\n"
        f"Rephrased Query: 'Retrieve CVE entries where severity is \"CRITICAL\" and software_component is \"Linux kernel\".'\n\n"

        f"User Query: '{user_query}'\n\n"
        f"Please rephrase this query, applying relevant semantic mappings and ensuring it aligns with the database schema. "
        f"Return only the rephrased query text.\n\n"

        f"Additional Rules:\n"
        f"1) Handle common misspellings and typos by using fuzzy matching on terms to map correctly to database schema attributes.\n"
        f"2) When a term is ambiguous (e.g., 'apple,' which could refer to the vendor or operating system): use context from other terms in the query (like 'OS' or 'software') to determine the correct mapping. "
        f"If the context is unclear, prioritize the most common mapping.\n"
        f"3) Strip all explanatory text and return only the rephrased query in Neo4j-compatible syntax.\n"
        f"4) Standardize relationship queries, using proper Neo4j syntax to accurately reflect database relationships, such as '(:CVE)-[:AFFECTS_PROTOCOL]->(:Protocol)'.\n\n"
        f"5) If the user query does not specify certain key attributes (such as severity, OS, or software components), "
        f"either make educated assumptions based on the common context or return the query with only the available terms. "
        f"For example, if only 'Oracle' is mentioned, rephrase the query to focus on 'Vendor' in the database schema and leave other criteria unspecified unless the context suggests otherwise.\n"
    )


    prompt = (
        f"You are a language model tasked with rephrasing user queries to align them with a Neo4j database schema. "
        f"Additionally, apply semantic mapping to ensure the query uses database-recognized terminology for key attributes. Follow these steps:\n\n"

        f"1) Identify the core intent and entities in the user query, including severity levels, operating systems, software components, and impact types.\n"
        f"2) Use semantic mappings to translate user terms or synonyms to the precise terminology used in the database.\n"
        f"3) Rephrase the query to align with the database schema's syntax and structure, ensuring that terms like vendor and operating system are correctly mapped.\n\n"

        f"Database Schema:\n"
        f"Node Properties:\n"
        f"  - CVE: id, cvss_v2, SEVERITY, cwe_id, Operating_System, Software_Component, Impact, Vendor, Network_Requirements, "
        f"Affected_Protocols, Version, Authentication_Required, User_Interaction_Required, Privileges_Required, Affected_Hardware, cvss_v3\n"
        f"  - Protocol: name\n"
        f"Relationships:\n"
        f"  - (:CVE)-[:AFFECTS_PROTOCOL]->(:Protocol)\n\n"

        f"Mappings for Common Terms:\n"
        f"Severity Levels:\n"
        f"  - high, critical -> CRITICAL\n"
        f"  - medium -> MEDIUM\n"
        f"  - low -> LOW\n\n"

        f"Operating Systems:\n"
        f"  - apple, mac, mac os -> Mac OS X\n"
        f"  - microsoft, windows os -> Windows\n"
        f"  - android os -> Android\n"
        f"  - linux os, unix -> Linux\n"
        f"  - sun, oracle solaris -> Solaris\n"
        f"  - hp, hp ux -> HP-UX\n\n"

        f"Software Components:\n"
        f"  - internet explorer, ie -> Microsoft Internet Explorer\n"
        f"  - linux kernel -> Linux kernel\n"
        f"  - webkit engine -> WebKit\n"
        f"  - edge browser -> Microsoft Edge\n"
        f"  - java, java se -> Oracle Java SE\n\n"

        f"Impact Types:\n"
        f"  - denial, dos -> denial of service\n"
        f"  - remote code execution, arbitrary code execution -> execute arbitrary code\n"
        f"  - sql injection, sql commands -> execute arbitrary SQL commands\n"
        f"  - xss, html injection -> arbitrary web script or HTML injection\n"
        f"  - privilege escalation, local escalation -> local escalation of privilege\n\n"

        f"Examples:\n"
        f"User Query: 'find vulnerabilities with high risk on mac computers.'\n"
        f"Rephrased Query: 'Retrieve CVE entries where severity is \"CRITICAL\" and operating_system is \"Mac OS X\".'\n\n"

        f"User Query: 'show denial vulnerabilities on windows'\n"
        f"Rephrased Query: 'Retrieve CVE entries where impact is \"denial of service\" and operating_system is \"Windows\".'\n\n"

        f"User Query: 'list critical exploits affecting linux kernel.'\n"
        f"Rephrased Query: 'Retrieve CVE entries where severity is \"CRITICAL\" and software_component is \"Linux kernel\".'\n\n"

        f"User Query: '{user_query}'\n\n"
        f"Please rephrase this query, applying relevant semantic mappings and ensuring it aligns with the database schema. "
        f"Return only the rephrased query text.\n\n"

        f"Additional Rules:\n"
        f"1) Handle common misspellings and typos by using fuzzy matching on terms to map correctly to database schema attributes.\n"
        f"2) When a term is ambiguous (e.g., 'apple,' which could refer to the vendor or operating system): use context from other terms in the query (like 'OS' or 'software') to determine the correct mapping. "
        f"If the context is unclear, prioritize the most common mapping.\n"
        f"3) Strip all explanatory text and return only the rephrased query in Neo4j-compatible syntax.\n"
        f"4) Standardize relationship queries, using proper Neo4j syntax to accurately reflect database relationships, such as '(:CVE)-[:AFFECTS_PROTOCOL]->(:Protocol)'.\n\n"
        f"5) If the user query includes terms like 'how I can be safe' or other actionable steps, please omit them as they are not part of the database schema. Focus only on the technical aspects related to CVE and impact.\n"
        f"6) If the user does not provide additional attributes such as severity or OS explicitly, the query should still be rephrased as accurately as possible with available data, and leave unspecified attributes where necessary (e.g., 'Retrieve CVE entries where vendor is \"Apple\"').\n"
    )

prompt = (
f"You are a language model tasked with rephrasing user queries to align them with a Neo4j database schema. "
f"Additionally, apply semantic mapping to ensure the query uses database-recognized terminology for key attributes. Follow these steps:\n\n"

    f"1) Identify the core intent and entities in the user query, including severity levels, operating systems, software components, and impact types.\n"
    f"2) Use semantic mappings to translate user terms or synonyms to the precise terminology used in the database.\n"
    f"3) Rephrase the query to align with the database schema's syntax and structure, ensuring that terms like vendor, operating system, and hardware are correctly mapped without making assumptions about unspecified attributes.\n\n"

    f"Database Schema:\n"
    f"Node Properties:\n"
    f"  - CVE: id, cvss_v2, SEVERITY, cwe_id, Operating_System, Software_Component, Impact, Vendor, Network_Requirements, "
    f"Affected_Protocols, Version, Authentication_Required, User_Interaction_Required, Privileges_Required, Affected_Hardware, cvss_v3\n"
    f"  - Protocol: name\n"
    f"Relationships:\n"
    f"  - (:CVE)-[:AFFECTS_PROTOCOL]->(:Protocol)\n\n"

    f"Mappings for Common Terms:\n"
    f"Severity Levels:\n"
    f"  - high, critical -> CRITICAL\n"
    f"  - medium -> MEDIUM\n"
    f"  - low -> LOW\n\n"

    f"Operating Systems:\n"
    f"  - apple, mac, mac os -> Mac OS X\n"
    f"  - microsoft, windows os -> Windows\n"
    f"  - android os -> Android\n"
    f"  - linux os, unix -> Linux\n"
    f"  - sun, oracle solaris -> Solaris\n"
    f"  - hp, hp ux -> HP-UX\n\n"

    f"Software Components:\n"
    f"  - internet explorer, ie -> Microsoft Internet Explorer\n"
    f"  - linux kernel -> Linux kernel\n"
    f"  - webkit engine -> WebKit\n"
    f"  - edge browser -> Microsoft Edge\n"
    f"  - java, java se -> Oracle Java SE\n\n"

    f"Impact Types:\n"
    f"  - denial, dos -> denial of service\n"
    f"  - remote code execution, arbitrary code execution -> execute arbitrary code\n"
    f"  - sql injection, sql commands -> execute arbitrary SQL commands\n"
    f"  - xss, html injection -> arbitrary web script or HTML injection\n"
    f"  - privilege escalation, local escalation -> local escalation of privilege\n\n"

    f"Examples:\n"
    f"User Query: 'find vulnerabilities with high risk on mac computers.'\n"
    f"Rephrased Query: 'Retrieve CVE entries where severity is \"CRITICAL\" and operating_system is \"Mac OS X\".'\n\n"

    f"User Query: 'show denial vulnerabilities on windows'\n"
    f"Rephrased Query: 'Retrieve CVE entries where impact is \"denial of service\" and operating_system is \"Windows\".'\n\n"

    f"User Query: 'list critical exploits affecting linux kernel.'\n"
    f"Rephrased Query: 'Retrieve CVE entries where severity is \"CRITICAL\" and software_component is \"Linux kernel\".'\n\n"

    f"User Query: '{user_query}'\n\n"
    f"Please rephrase this query, applying relevant semantic mappings and ensuring it aligns with the database schema. "
    f"Return only the rephrased query text.\n\n"

    f"Additional Rules:\n"
    f"1) Handle common misspellings and typos by using fuzzy matching on terms to map correctly to database schema attributes.\n"
    f"2) When a term is ambiguous (e.g., 'apple,' which could refer to the vendor or operating system): use context from other terms in the query (like 'OS' or 'software') to determine the correct mapping. "
    f"If the context is unclear, prioritize the most common mapping.\n"
    f"3) If the query mentions hardware or peripheral devices (e.g., 'USB drives'), do not force an operating system mapping. Instead, focus on relevant properties such as hardware and related vulnerabilities.\n"
    f"4) Avoid making assumptions about attributes (such as vendor) if the user has not specified them. Only add such attributes if explicitly mentioned in the query.\n"
    f"5) Strip all explanatory text and return only the rephrased query in Neo4j-compatible syntax.\n"

)
