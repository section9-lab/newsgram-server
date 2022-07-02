package com.github.dnsinsight.controller;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

/**
 * @Author: Tachikoma
 * @Date: 2022-07-02 10:02
 * @Description:
 */
@RestController
public class DnsController {

    @GetMapping
    public String searchDnsInfo(){
        return "dns info test";
    }
}
