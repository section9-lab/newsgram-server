package com.github.dnsinsight.service;

import cn.hutool.core.util.RuntimeUtil;
import com.github.dnsinsight.controller.vo.DnsInfoVo;
import lombok.extern.slf4j.Slf4j;
import org.springframework.stereotype.Service;

import java.util.List;

/**
 * @Author: Tachikoma
 * @Date: 2022-07-02 10:43
 * @Description:
 */
@Service
@Slf4j
public class DnsService {
    public DnsInfoVo findDnsInfo(String domain) {

        List<String> aa = RuntimeUtil.execForLines("dig +short aa" + domain);
        List<String> aaaa = RuntimeUtil.execForLines("dig +short aaaa" + domain);
        List<String> ns = RuntimeUtil.execForLines("dig +short ns" + domain);
        List<String> mx = RuntimeUtil.execForLines("dig +short mx" + domain);
        List<String> cname = RuntimeUtil.execForLines("dig +short cname" + domain);

        return DnsInfoVo.builder().build()
                .setAa(aa)
                .setAaaa(aaaa)
                .setNs(ns)
                .setMx(mx)
                .setCname(cname);
    }
}
