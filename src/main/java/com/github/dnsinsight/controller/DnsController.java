package com.github.dnsinsight.controller;

import com.github.dnsinsight.service.DnsService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

/**
 * @Author: Tachikoma
 * @Date: 2022-07-02 10:02
 * @Description:
 */
@RestController
public class DnsController {

    @Autowired
    private DnsService dnsService;

    @GetMapping("/dns-info")
    public List<String> searchDnsInfo(@RequestParam String domain){
        return dnsService.findDnsInfo(domain);
    }
}
